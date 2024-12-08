import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": ""
})

ref = db.reference('Students')

data = {
    "298976":
        {
            "name": "Virat Kohli",
            "major": "Cricket",
            "starting_year": "2010",
            "total_attendance": "4",
            "standing": "G",
            "year": "4",
            "last_attendance_time": "2024-12-07 00:54:34"
        },
    "519090":
        {
            "name": "Bill Gates",
            "major": "Computer Science",
            "starting_year": "2009",
            "total_attendance": "7",
            "standing": "G",
            "year": "3",
            "last_attendance_time": "2024-12-07 00:54:34"
        },
    "567623":
        {
            "name": "Kavindu Disnaka",
            "major": "Computer Science",
            "starting_year": "2021",
            "total_attendance": "6",
            "standing": "G",
            "year": "4",
            "last_attendance_time": "2024-12-07 00:54:34"
        },
    "852741":
        {
            "name": "Emly Blunt",
            "major": "Economics",
            "starting_year": "2021",
            "total_attendance": "12",
            "standing": "B",
            "year": "1",
            "last_attendance_time": "2024-12-07 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": "2020",
            "total_attendance": "9",
            "standing": "G",
            "year": "2",
            "last_attendance_time": "2024-12-07 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)  # Use .child(key) instead of .push(key)
