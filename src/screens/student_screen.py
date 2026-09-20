# import streamlit as st

# from src.ui.base_layout import style_background_dashboard, style_base_layout

# from src.components.header import header_dashboard
# from src.components.footer import footer_dashboard
# from PIL import Image            #PIL ---> Pillow library
# import numpy as np
# from src.pipelines.face_pipeline import predict_attendance, get_face_embeddings, train_classifier
# from src.pipelines.voice_pipeline import get_voice_embedding
# from src.database.db import get_all_students, create_student, get_student_subjects, get_student_attendance, unenroll_student_to_subject
# import time

# from src.components.dialog_enroll import enroll_dialog
# from src.components.subject_card import subject_card


# def student_dashboard():
#     student_data = st.session_state.student_data
#     student_id = student_data['student_id']
#     c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
#     with c1:
#         header_dashboard()
#     with c2:
#         st.subheader(f"""Welcome, {student_data['name']} """)
#         if st.button("Logout", type='secondary', key='loginbackbtn', shortcut="control+backspace"):
#             st.session_state['is_logged_in'] = False
#             del st.session_state.student_data 
#             st.rerun()


#     st.space()

#     c1, c2 =st.columns(2)
#     with c1:
#         st.header('Your Enrolled Subjects')
#     with c2:
#         if st.button('Enroll in Subject', type='primary', width='stretch'):
#             enroll_dialog()


#     st.divider()


#     with st.spinner('Loading your enrolled subjects..'):
#         subjects = get_student_subjects(student_id)
#         logs = get_student_attendance(student_id)

#     stats_map = {}

#     for log in logs:
#         sid = log['subject_id']

#         if sid not in stats_map:
#             stats_map[sid] = {"total":0, "attendance":0}

#         stats_map[sid]['total'] +=1

#         if logs.get('is_present'):
#             stats_map[sid]['attend'] += 1

#     cols = st.columns(2)
#     for i, sub_node in enumerate(subjects):
#         sub = sub_node['subjects']
#         sid = sub['subject_id']

#         stats = stats_map.get(sid,{"total":0, "attended":0})
#         def unenroll_button():
#             if st.button("Unenroll from this course", type='tertiary', width='stretch', icon=':material/delete_forever:'):
#                 unenroll_student_to_subject(student_id, sid)
#                 st.toast(f'Unenrolled from {sub['name']} successfully!')
#                 st.rerun()

#         with cols[i % 2]:
#             subject_card(
#                 name = sub["name"],
#                 code = sub["subject_code"],
#                 section = sub['section'],
#                 stats = [
#                     ('📅', 'Total', stats['total']),
#                     ('✅', 'Attended', stats['attended']),
#                 ],
#             )
#     footer_dashboard()





# def student_screen():
#     style_background_dashboard()
#     style_base_layout()

#     if "student_data" in st.session_state:
#         student_dashboard()
#         return

#     c1, c2 = st.columns(2, vertical_alignment='center', gap='large')
#     with c1:
#         header_dashboard()
#     with c2:
#         if st.button("Go back to Home", type='secondary', key='login_back_btn', shortcut='control+backspace'):
#             st.session_state['login_type'] = None
#             st.rerun()

#     st.header('Login Using FaceID', text_alignment='center')
#     st.space()
#     st.space()

#     show_registration = False
#     photo_source = st.camera_input("Position your face in the Center")
#     # Pass a fixed key parameter to lock the media stream instance
#     #photo_source = st.camera_input("Position your face in the Center", key="student_login_cam")
    
#     if photo_source:
#         img = np.array(Image.open(photo_source))

#         with st.spinner('AI is scanning..'):
#             detected, all_ids, num_faces = predict_attendance(img)

#             if num_faces == 0:
#                 st.warning('Face not found!')
#             elif num_faces > 1:
#                 st.warning('Multiple faces found')
#             else:
#                 if detected:
#                     student_id = list(detected.keys())[0]
#                     all_students = get_all_students()
#                     student = next((s for s in all_students if s['student_id']==student_id), None)

#                     if student:
#                         st.session_state.is_logged_in = True
#                         st.session_state.user_role = 'student'
#                         st.session_state.student_data = student
#                         st.toast(f"Welcome Back {student['name']}")
#                         time.sleep(1)
#                         st.rerun()
#                 else:
#                     st.info('Face not recognized! You might be a new student!')
#                     show_registration = True

#     if show_registration:
#         with st.container(border=True):
#             st.header('Register New Profile')
#             new_name = st.text_input("Enter your name", placeholder='Enter Your Name')

#             st.subheader('Optional : Voice Enrollment')
#             st.info("Enroll your for voice only attendance")

#             audio_data = None

#             try:
#                 audio_data = st.audio_input('Record a Short phrase like I am present, My name is Alam.')
#             except Exception:
#                 st.error("Audio Data failed!")
            

#             if st.button('Create Account', type='primary'):
#                 if new_name:
#                     with st.spinner('Creating Profile..'):
#                         img = np.array(Image.open(photo_source))
#                         encodings = get_face_embeddings(img)
#                         if encodings:
#                             face_emb = encodings[0].tolist()

#                             voice_emb = None
#                             if audio_data:
#                                 voice_emb = get_voice_embedding(audio_data.read())

#                             response_data = create_student(new_name, face_embedding=face_emb, voice_embedding=voice_emb)

#                             if response_data:
#                                 train_classifier()
#                                 st.session_state.is_logged_in = True
#                                 st.session_state.user_role = 'student'
#                                 st.session_state.student_data = response_data[0]
#                                 st.toast(f"Profile Created! Hi {new_name}!")
#                                 time.sleep(1)
#                                 st.rerun()
#                         else:
#                             st.error("Couldn't capture your facial feature for registration")


#                 else:
#                     st.warning("Please enter your name!")

#     footer_dashboard()






























# import streamlit as st
# import numpy as np
# import time
# from PIL import Image

# from src.ui.base_layout import style_background_dashboard, style_base_layout
# from src.components.header import header_dashboard
# from src.components.footer import footer_dashboard
# from src.components.dialog_enroll import enroll_dialog
# from src.components.subject_card import subject_card

# from src.pipelines.face_pipeline import predict_attendance, get_face_embeddings, train_classifier
# from src.pipelines.voice_pipeline import get_voice_embedding
# from src.database.db import (
#     get_all_students, 
#     create_student, 
#     get_student_subjects, 
#     get_student_attendance, 
#     unenroll_student_to_subject
# )

# def student_dashboard():
#     student_data = st.session_state.student_data
#     student_id = student_data['student_id']
#     c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
#     with c1:
#         header_dashboard()
#     with c2:
#         st.subheader(f"""Welcome, {student_data['name']} """)
#         if st.button("Logout", type='secondary', key='loginbackbtn', shortcut="control+backspace"):
#             st.session_state['is_logged_in'] = False
#             if 'student_data' in st.session_state:
#                 del st.session_state.student_data 
#             if 'show_registration' in st.session_state:
#                 st.session_state.show_registration = False
#             st.rerun()

#     st.space()

#     c1, c2 = st.columns(2)
#     with c1:
#         st.header('Your Enrolled Subjects')
#     with c2:
#         if st.button('Enroll in Subject', type='primary', width='stretch'):
#             enroll_dialog()

#     st.divider()

#     with st.spinner('Loading your enrolled subjects..'):
#         subjects = get_student_subjects(student_id)
#         logs = get_student_attendance(student_id)

#     stats_map = {}

#     for log in logs:
#         sid = log['subject_id']

#         if sid not in stats_map:
#             stats_map[sid] = {"total": 0, "attended": 0}

#         stats_map[sid]['total'] += 1

#         if log.get('is_present'):
#             stats_map[sid]['attended'] += 1

#     cols = st.columns(2)
#     for i, sub_node in enumerate(subjects):
#         sub = sub_node['subjects']
#         sid = sub['subject_id']

#         stats = stats_map.get(sid, {"total": 0, "attended": 0})

#         with cols[i % 2]:
#             subject_card(
#                 name=sub["name"],
#                 code=sub["subject_code"],
#                 section=sub['section'],
#                 stats=[
#                     ('📅', 'Total', stats['total']),
#                     ('✅', 'Attended', stats['attended']),
#                 ],
#             )
#             if st.button("Unenroll from this course", key=f"unenroll_{sid}", type='tertiary', width='stretch', icon=':material/delete_forever:'):
#                 unenroll_student_to_subject(student_id, sid)
#                 st.toast(f"Unenrolled from {sub['name']} successfully!")
#                 st.rerun()

#     footer_dashboard()


# def student_screen():
#     style_background_dashboard()
#     style_base_layout()

#     if "student_data" in st.session_state:
#         student_dashboard()
#         return

#     # Keep track of registration state across script reruns
#     if 'show_registration' not in st.session_state:
#         st.session_state.show_registration = False

#     c1, c2 = st.columns(2, vertical_alignment='center', gap='large')
#     with c1:
#         header_dashboard()
#     with c2:
#         if st.button("Go back to Home", type='secondary', key='login_back_btn', shortcut='control+backspace'):
#             st.session_state['login_type'] = None
#             st.session_state.show_registration = False
#             st.rerun()

#     st.header('Login Using FaceID', text_alignment='center')
#     st.space()
#     st.space()

#     # Replaced camera_input with file_uploader to allow device file selection/camera uploads
#     photo_source = st.file_uploader(
#         "Upload or capture a clear selfie photo from your device", 
#         type=["jpg", "jpeg", "png"],
#         key="student_selfie_upload"
#     )
    
#     if photo_source:
#         img = np.array(Image.open(photo_source))

#         with st.spinner('AI is scanning..'):
#             detected, all_ids, num_faces = predict_attendance(img)

#             if num_faces == 0:
#                 st.warning('Face not found!')
#                 st.session_state.show_registration = False
#             elif num_faces > 1:
#                 st.warning('Multiple faces found')
#                 st.session_state.show_registration = False
#             else:
#                 if detected:
#                     st.session_state.show_registration = False
#                     student_id = list(detected.keys())[0]
#                     all_students = get_all_students()
#                     student = next((s for s in all_students if s['student_id'] == student_id), None)

#                     if student:
#                         st.session_state.is_logged_in = True
#                         st.session_state.user_role = 'student'
#                         st.session_state.student_data = student
#                         st.toast(f"Welcome Back {student['name']}")
#                         time.sleep(1)
#                         st.rerun()
#                 else:
#                     st.info('Face not recognized! You might be a new student!')
#                     st.session_state.show_registration = True

#     if st.session_state.show_registration:
#         with st.container(border=True):
#             st.header('Register New Profile')
#             new_name = st.text_input("Enter your name", placeholder='Enter Your Name')

#             st.subheader('Optional : Voice Enrollment')
#             st.info("Enroll your voice for voice-only attendance")

#             audio_data = None

#             try:
#                 audio_data = st.audio_input('Record a Short phrase like "I am present, My name is Alam."')
#             except Exception:
#                 st.error("Audio Data failed!")

#             if st.button('Create Account', type='primary'):
#                 if new_name:
#                     if photo_source is not None:
#                         with st.spinner('Creating Profile..'):
#                             img = np.array(Image.open(photo_source))
#                             encodings = get_face_embeddings(img)
#                             if encodings:
#                                 face_emb = encodings[0].tolist()

#                                 voice_emb = None
#                                 if audio_data:
#                                     voice_emb = get_voice_embedding(audio_data.read())

#                                 response_data = create_student(new_name, face_embedding=face_emb, voice_embedding=voice_emb)

#                                 if response_data:
#                                     train_classifier()
#                                     st.session_state.is_logged_in = True
#                                     st.session_state.user_role = 'student'
#                                     st.session_state.student_data = response_data[0]
#                                     st.session_state.show_registration = False
#                                     st.toast(f"Profile Created! Hi {new_name}!")
#                                     time.sleep(1)
#                                     st.rerun()
#                             else:
#                                 st.error("Couldn't capture your facial feature for registration")
#                     else:
#                         st.error("Please upload a selfie photo to register!")
#                 else:
#                     st.warning("Please enter your name!")

#     footer_dashboard()

































import streamlit as st
import numpy as np
import time
from PIL import Image

from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from src.components.dialog_enroll import enroll_dialog
from src.components.subject_card import subject_card

from src.pipelines.face_pipeline import predict_attendance, get_face_embeddings, train_classifier
from src.pipelines.voice_pipeline import get_voice_embedding
from src.database.db import (
    get_all_students, 
    create_student, 
    get_student_subjects, 
    get_student_attendance, 
    unenroll_student_to_subject
)

def student_dashboard():
    student_data = st.session_state.student_data
    student_id = student_data['student_id']
    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        st.subheader(f"""Welcome, {student_data['name']} """)
        if st.button("Logout", type='secondary', key='loginbackbtn', shortcut="control+backspace"):
            st.session_state['is_logged_in'] = False
            if 'student_data' in st.session_state:
                del st.session_state.student_data 
            if 'show_registration' in st.session_state:
                st.session_state.show_registration = False
            st.rerun()

    st.space()

    c1, c2 = st.columns(2)
    with c1:
        st.header('Your Enrolled Subjects')
    with c2:
        if st.button('Enroll in Subject', type='primary', width='stretch'):
            enroll_dialog()

    st.divider()

    with st.spinner('Loading your enrolled subjects..'):
        subjects = get_student_subjects(student_id)
        logs = get_student_attendance(student_id)

    stats_map = {}

    for log in logs:
        sid = log['subject_id']

        if sid not in stats_map:
            stats_map[sid] = {"total": 0, "attended": 0}

        stats_map[sid]['total'] += 1

        if log.get('is_present'):
            stats_map[sid]['attended'] += 1

    cols = st.columns(2)
    for i, sub_node in enumerate(subjects):
        sub = sub_node['subjects']
        sid = sub['subject_id']

        stats = stats_map.get(sid, {"total": 0, "attended": 0})

        with cols[i % 2]:
            subject_card(
                name=sub["name"],
                code=sub["subject_code"],
                section=sub['section'],
                stats=[
                    ('📅', 'Total', stats['total']),
                    ('✅', 'Attended', stats['attended']),
                ],
            )
            if st.button("Unenroll from this course", key=f"unenroll_{sid}", type='tertiary', width='stretch', icon=':material/delete_forever:'):
                unenroll_student_to_subject(student_id, sid)
                st.toast(f"Unenrolled from {sub['name']} successfully!")
                st.rerun()

    footer_dashboard()


def student_screen():
    style_background_dashboard()
    style_base_layout()

    if "student_data" in st.session_state:
        student_dashboard()
        return

    # Keep track of registration state across script reruns
    if 'show_registration' not in st.session_state:
        st.session_state.show_registration = False

    c1, c2 = st.columns(2, vertical_alignment='center', gap='large')
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to Home", type='secondary', key='login_back_btn', shortcut='control+backspace'):
            st.session_state['login_type'] = None
            st.session_state.show_registration = False
            st.rerun()

    st.header('Login Using FaceID', text_alignment='center')
    st.space()

    # Styling for uniform container height and alignment
    st.markdown("""
        <style>
            div[data-testid="stFileUploader"] {
                width: 100%;
                max-width: 700px;
                margin: 0 auto;
            }
            div[data-testid="stFileUploader"] section {
                padding: 2.5rem 1.5rem;
                border-radius: 12px;
                min-height: 280px;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
            }
        </style>
    """, unsafe_allow_html=True)

    photo_source = None

    # Dual input selection: Camera or Upload
    _, center_col, _ = st.columns([1, 4, 1])

    with center_col:
        tab_cam, tab_file = st.tabs(["📷 Take Photo", "📁 Upload Selfie File"])

        with tab_cam:
            cam_photo = st.camera_input("Position your face in the Center", key="student_cam_input")
            if cam_photo:
                photo_source = cam_photo

        with tab_file:
            file_photo = st.file_uploader(
                "Select a clear selfie image from your device", 
                type=["jpg", "jpeg", "png"],
                key="student_selfie_upload"
            )
            if file_photo:
                st.image(file_photo, use_container_width=True, caption="Uploaded Selfie Preview")
                photo_source = file_photo

    if photo_source:
        img = np.array(Image.open(photo_source))

        with st.spinner('AI is scanning..'):
            detected, all_ids, num_faces = predict_attendance(img)

            if num_faces == 0:
                st.warning('Face not found!')
                st.session_state.show_registration = False
            elif num_faces > 1:
                st.warning('Multiple faces found')
                st.session_state.show_registration = False
            else:
                if detected:
                    st.session_state.show_registration = False
                    student_id = list(detected.keys())[0]
                    all_students = get_all_students()
                    student = next((s for s in all_students if s['student_id'] == student_id), None)

                    if student:
                        st.session_state.is_logged_in = True
                        st.session_state.user_role = 'student'
                        st.session_state.student_data = student
                        st.toast(f"Welcome Back {student['name']}")
                        time.sleep(1)
                        st.rerun()
                else:
                    st.info('Face not recognized! You might be a new student!')
                    st.session_state.show_registration = True

    if st.session_state.show_registration:
        with st.container(border=True):
            st.header('Register New Profile')
            new_name = st.text_input("Enter your name", placeholder='Enter Your Name')

            st.subheader('Optional : Voice Enrollment')
            st.info("Enroll your voice for voice-only attendance")

            audio_data = None

            try:
                audio_data = st.audio_input('Record a Short phrase like "I am present, My name is Alam."')
            except Exception:
                st.error("Audio Data failed!")

            if st.button('Create Account', type='primary'):
                if new_name:
                    if photo_source is not None:
                        with st.spinner('Creating Profile..'):
                            img = np.array(Image.open(photo_source))
                            encodings = get_face_embeddings(img)
                            if encodings:
                                face_emb = encodings[0].tolist()

                                voice_emb = None
                                if audio_data:
                                    voice_emb = get_voice_embedding(audio_data.read())

                                response_data = create_student(new_name, face_embedding=face_emb, voice_embedding=voice_emb)

                                if response_data:
                                    train_classifier()
                                    st.session_state.is_logged_in = True
                                    st.session_state.user_role = 'student'
                                    st.session_state.student_data = response_data[0]
                                    st.session_state.show_registration = False
                                    st.toast(f"Profile Created! Hi {new_name}!")
                                    time.sleep(1)
                                    st.rerun()
                            else:
                                st.error("Couldn't capture your facial feature for registration")
                    else:
                        st.error("Please capture or upload a selfie photo to register!")
                else:
                    st.warning("Please enter your name!")

    footer_dashboard()