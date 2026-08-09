"""
AI Smart Civic Services - Flask REST API & Backend Web Server
Author: Akash Ahmed (SMIT Hackathon Contestant)
"""

from flask import Flask, render_template, request, jsonify
from models import DatabaseManager, AIAnalyzer, ComplaintManager, StatsCalculator, NotificationManager
import os

app = Flask(__name__, template_folder="templates", static_folder="static")

# Initialize OOP Architecture Components
db_manager = DatabaseManager("civic_services.db")
ai_analyzer = AIAnalyzer()
complaint_manager = ComplaintManager(db_manager, ai_analyzer)


@app.route("/")
def index():
    """Renders the main web portal for citizens and administrators."""
    return render_template("index.html")


@app.route("/api/login", methods=["POST"])
def login():
    """Role-based authentication endpoint for Citizens and Admins."""
    data = request.json or {}
    email = data.get("email", "").strip().lower()
    password = data.get("password", "").strip()
    role = data.get("role", "citizen").strip().lower()

    if not email or not password:
        return jsonify({"success": False, "error": "Email/Username and Password are required."}), 400

    if role == "admin":
        if ("admin" in email) and (password in ["admin", "1234", "123", "admin123"]):
            return jsonify({
                "success": True,
                "role": "admin",
                "message": "Admin Login Successful!",
                "user": {
                    "name": "Admin Operations Officer",
                    "email": "admin@civic.gov",
                    "department": "Municipal Service Command"
                }
            })
        else:
            return jsonify({"success": False, "error": "Invalid Admin credentials. Use 'admin' / 'admin'"}), 401
    else:
        name = email.split('@')[0].replace('.', ' ').title() if '@' in email else "Akash Ahmed"
        return jsonify({
            "success": True,
            "role": "citizen",
            "message": "Citizen Login Successful!",
            "user": {
                "name": name if name else "Akash Ahmed",
                "email": email,
                "contact": "0300-1234567"
            }
        })


@app.route("/api/analyze-ai", methods=["POST"])
def analyze_ai():
    """Real-time AI prediction endpoint for instant live preview as user types."""
    data = request.json or {}
    title = data.get("title", "")
    description = data.get("description", "")
    has_image = bool(data.get("image_url"))

    if not title and not description:
        return jsonify({"error": "Title or description required for AI analysis"}), 400

    analysis = ai_analyzer.analyze_complaint(title, description, has_image)
    return jsonify({
        "success": True,
        "analysis": analysis
    })


@app.route("/api/complaints", methods=["GET"])
def get_complaints():
    """Get all complaints with optional filtering & search."""
    category = request.args.get("category")
    priority = request.args.get("priority")
    status = request.args.get("status")
    search = request.args.get("search")

    complaints = db_manager.get_all_complaints(
        category=category,
        priority=priority,
        status=status,
        search=search
    )
    return jsonify({
        "success": True,
        "count": len(complaints),
        "complaints": [c.to_dict() for c in complaints]
    })


@app.route("/api/complaints", methods=["POST"])
def create_complaint():
    """Submit a new citizen complaint with automated AI analysis & DB persistence."""
    data = request.json or {}
    title = data.get("title", "").strip()
    description = data.get("description", "").strip()

    if not title or not description:
        return jsonify({"success": False, "error": "Title and description are required fields."}), 400

    new_complaint = complaint_manager.submit_new_complaint(data)
    notification = NotificationManager.notify_status_change(new_complaint)

    return jsonify({
        "success": True,
        "message": "Complaint submitted successfully and processed by AI!",
        "complaint": new_complaint.to_dict(),
        "notification": notification
    }), 201


@app.route("/api/complaints/<int:complaint_id>", methods=["GET"])
def get_complaint(complaint_id):
    """Retrieve single complaint details."""
    complaint = db_manager.get_complaint_by_id(complaint_id)
    if not complaint:
        return jsonify({"success": False, "error": "Complaint not found"}), 404
    return jsonify({"success": True, "complaint": complaint.to_dict()})


@app.route("/api/complaints/<int:complaint_id>", methods=["PUT"])
def update_complaint(complaint_id):
    """Update complaint status or assigned department."""
    data = request.json or {}
    status = data.get("status")
    department = data.get("assigned_department")

    if not status:
        return jsonify({"success": False, "error": "Status is required"}), 400

    updated = db_manager.update_complaint_status(complaint_id, status, department)
    if not updated:
        return jsonify({"success": False, "error": "Failed to update complaint"}), 404

    complaint = db_manager.get_complaint_by_id(complaint_id)
    notification = NotificationManager.notify_status_change(complaint) if complaint else ""

    return jsonify({
        "success": True,
        "message": f"Complaint #{complaint_id} updated to {status}",
        "notification": notification
    })


@app.route("/api/complaints/<int:complaint_id>", methods=["DELETE"])
def delete_complaint(complaint_id):
    """Remove a complaint from system."""
    deleted = db_manager.delete_complaint(complaint_id)
    if not deleted:
        return jsonify({"success": False, "error": "Complaint not found"}), 404
    return jsonify({"success": True, "message": f"Complaint #{complaint_id} deleted."})


@app.route("/api/stats", methods=["GET"])
def get_stats():
    """Return statistical analytics calculations for charts and reports."""
    stats = complaint_manager.get_statistics()
    return jsonify({"success": True, "stats": stats})


@app.route("/api/chatbot", methods=["POST"])
def chatbot():
    """AI Civic Assistant chatbot endpoint."""
    data = request.json or {}
    query = data.get("query", "").strip()
    if not query:
        return jsonify({"success": False, "answer": "Please type a question about civic services or your rights."})

    answer = ai_analyzer.answer_chatbot_query(query)
    return jsonify({"success": True, "answer": answer})


if __name__ == "__main__":
    print("==========================================================")
    print("[INFO] AI Smart Civic Services Platform is launching...")
    print("[INFO] Access web portal at: http://127.0.0.1:5000")
    print("==========================================================")
    app.run(host="0.0.0.0", port=5000, debug=True)
