# 📸 Snap Class AI - Smart Attendance System

An AI-powered automated attendance system built with Streamlit, OpenCV, and Deep Learning models. The platform allows modern educational institutions to conduct seamless student attendance via facial recognition and voice biometric verification.

---

## ✨ Features

- **Dual-Mode Student Verification:**
  - 📷 **FaceID Authentication:** Instant face detection & embedding matching for seamless student login and attendance.
  - 🎙️ **Voice Biometrics:** Voice embedding extraction for recording audio and verifying students via phrase recognition.
- **Flexible Student Portal:**
  - Live camera photo capture or selfie file upload options for verification.
  - Course enrollment and unenrolling dashboard.
  - Real-time attendance tracking and statistical overview per enrolled course.
- **Teacher Dashboard:**
  - Course creation, subject management, and student roster overview.
  - Bulk classroom audio analysis for hands-free group voice attendance.
  - Automated logging into Supabase cloud database.

---

## 🛠️ Tech Stack

- **Frontend / Web UI:** Streamlit
- **Computer Vision & AI:** OpenCV, NumPy, Pillow, PyTorch / Deep Learning Pipelines
- **Database & Cloud Storage:** Supabase (PostgreSQL)
- **Data Manipulation:** Pandas

---

## 📁 Project Structure

```text
├── app.py                             # Application entry point
├── requirements.txt                   # Python dependencies
├── src/
│   ├── components/                    # Reusable Streamlit UI components & dialogs
│   │   ├── dialog_attendance_results.py
│   │   ├── dialog_enroll.py
│   │   ├── dialog_voice_attendance.py
│   │   ├── footer.py
│   │   ├── header.py
│   │   └── subject_card.py
│   ├── database/                      # Supabase configuration & database CRUD functions
│   │   ├── config.py
│   │   └── db.py
│   ├── pipelines/                     # AI/ML inference pipelines
│   │   ├── face_pipeline.py           # Face detection, embedding extraction, & classification
│   │   └── voice_pipeline.py          # Voice embedding processing & bulk audio analysis
│   ├── screens/                       # Main application view screens
│   │   ├── student_screen.py
│   │   └── teacher_screen.py
│   └── ui/                            # Base CSS layout & theme styling
│       └── base_layout.py
