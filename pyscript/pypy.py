import psycopg2
import json


# data = [
#   {
#     "id": 1,
#     "college_name": "Greenfield University",
#     "courses": [
#       {"course_name": "Computer Science", "price": 80000, "enrollment": 200},
#       {"course_name": "Mechanical Engineering", "price": 75000, "enrollment": 150},
#       {"course_name": "Civil Engineering", "price": 70000, "enrollment": 180}
#     ],
#     "employees": 300
#   },
#   {
#     "id": 2,
#     "college_name": "Horizon Institute of Technology",
#     "courses": [
#       {"course_name": "Information Technology", "price": 82000, "enrollment": 210},
#       {"course_name": "Electrical Engineering", "price": 78000, "enrollment": 160},
#       {"course_name": "Chemical Engineering", "price": 72000, "enrollment": 190}
#     ],
#     "employees": 250
#   },
#   {
#     "id": 3,
#     "college_name": "Lakeside College",
#     "courses": [
#       {"course_name": "Biotechnology", "price": 85000, "enrollment": 180},
#       {"course_name": "Environmental Science", "price": 68000, "enrollment": 140},
#       {"course_name": "Mathematics", "price": 60000, "enrollment": 220}
#     ],
#     "employees": 200
#   },
#   {
#     "id": 4,
#     "college_name": "Silver Valley University",
#     "courses": [
#       {"course_name": "Physics", "price": 75000, "enrollment": 170},
#       {"course_name": "Chemistry", "price": 70000, "enrollment": 190},
#       {"course_name": "Biology", "price": 68000, "enrollment": 210}
#     ],
#     "employees": 280
#   },
#   {
#     "id": 5,
#     "college_name": "Mountain View Institute",
#     "courses": [
#       {"course_name": "Business Administration", "price": 90000, "enrollment": 250},
#       {"course_name": "Economics", "price": 85000, "enrollment": 230},
#       {"course_name": "Finance", "price": 88000, "enrollment": 220}
#     ],
#     "employees": 350
#   },
#   {
#     "id": 6,
#     "college_name": "Springfield University",
#     "courses": [
#       {"course_name": "Law", "price": 95000, "enrollment": 140},
#       {"course_name": "Political Science", "price": 70000, "enrollment": 130},
#       {"course_name": "International Relations", "price": 75000, "enrollment": 160}
#     ],
#     "employees": 270
#   },
#   {
#     "id": 7,
#     "college_name": "Riverside College",
#     "courses": [
#       {"course_name": "History", "price": 60000, "enrollment": 120},
#       {"course_name": "Philosophy", "price": 65000, "enrollment": 100},
#       {"course_name": "Sociology", "price": 70000, "enrollment": 140}
#     ],
#     "employees": 220
#   },
#   {
#     "id": 8,
#     "college_name": "Pine Hill University",
#     "courses": [
#       {"course_name": "Psychology", "price": 72000, "enrollment": 150},
#       {"course_name": "Education", "price": 68000, "enrollment": 170},
#       {"course_name": "Social Work", "price": 70000, "enrollment": 160}
#     ],
#     "employees": 260
#   },
#   {
#     "id": 9,
#     "college_name": "Maple Leaf College",
#     "courses": [
#       {"course_name": "Literature", "price": 62000, "enrollment": 140},
#       {"course_name": "Linguistics", "price": 65000, "enrollment": 120},
#       {"course_name": "Creative Writing", "price": 70000, "enrollment": 130}
#     ],
#     "employees": 230
#   },
#   {
#     "id": 10,
#     "college_name": "Cedar Point Institute",
#     "courses": [
#       {"course_name": "Architecture", "price": 88000, "enrollment": 180},
#       {"course_name": "Urban Planning", "price": 84000, "enrollment": 150},
#       {"course_name": "Interior Design", "price": 78000, "enrollment": 170}
#     ],
#     "employees": 290
#   },
#   {
#     "id": 11,
#     "college_name": "Sunrise University",
#     "courses": [
#       {"course_name": "Graphic Design", "price": 70000, "enrollment": 160},
#       {"course_name": "Fine Arts", "price": 68000, "enrollment": 150},
#       {"course_name": "Animation", "price": 72000, "enrollment": 140}
#     ],
#     "employees": 240
#   },
#   {
#     "id": 12,
#     "college_name": "Ocean View College",
#     "courses": [
#       {"course_name": "Marine Biology", "price": 90000, "enrollment": 110},
#       {"course_name": "Oceanography", "price": 85000, "enrollment": 100},
#       {"course_name": "Environmental Studies", "price": 80000, "enrollment": 120}
#     ],
#     "employees": 200
#   },
#   {
#     "id": 13,
#     "college_name": "Desert Oasis University",
#     "courses": [
#       {"course_name": "Geology", "price": 75000, "enrollment": 130},
#       {"course_name": "Environmental Geoscience", "price": 70000, "enrollment": 120},
#       {"course_name": "Hydrology", "price": 72000, "enrollment": 110}
#     ],
#     "employees": 210
#   },
#   {
#     "id": 14,
#     "college_name": "Highland Institute",
#     "courses": [
#       {"course_name": "Astronomy", "price": 80000, "enrollment": 140},
#       {"course_name": "Astrophysics", "price": 85000, "enrollment": 130},
#       {"course_name": "Space Science", "price": 78000, "enrollment": 120}
#     ],
#     "employees": 220
#   },
#   {
#     "id": 15,
#     "college_name": "Summit College",
#     "courses": [
#       {"course_name": "Data Science", "price": 95000, "enrollment": 250},
#       {"course_name": "Artificial Intelligence", "price": 98000, "enrollment": 230},
#       {"course_name": "Machine Learning", "price": 92000, "enrollment": 240}
#     ],
#     "employees": 330
#   },
#   {
#     "id": 16,
#     "college_name": "Prairie Institute of Technology",
#     "courses": [
#       {"course_name": "Cybersecurity", "price": 87000, "enrollment": 200},
#       {"course_name": "Network Engineering", "price": 82000, "enrollment": 180},
#       {"course_name": "Cloud Computing", "price": 89000, "enrollment": 190}
#     ],
#     "employees": 310
#   },
#   {
#     "id": 17,
#     "college_name": "Seaside University",
#     "courses": [
#       {"course_name": "Marine Engineering", "price": 91000, "enrollment": 120},
#       {"course_name": "Naval Architecture", "price": 88000, "enrollment": 100},
#       {"course_name": "Coastal Engineering", "price": 86000, "enrollment": 110}
#     ],
#     "employees": 190
#   },
#   {
#     "id": 18,
#     "college_name": "Forest View College",
#     "courses": [
#       {"course_name": "Forestry", "price": 70000, "enrollment": 130},
#       {"course_name": "Wildlife Conservation", "price": 75000, "enrollment": 140},
#       {"course_name": "Environmental Management", "price": 78000, "enrollment": 150}
#     ],
#     "employees": 220
#   },
#   {
#     "id": 19,
#     "college_name": "Crystal Lake University",
#     "courses": [
#       {"course_name": "Geography", "price": 67000, "enrollment": 150},
#       {"course_name": "Geospatial Science", "price": 72000, "enrollment": 130},
#       {"course_name": "Cartography", "price": 69000, "enrollment": 140}
#     ],
#     "employees": 210
#   }
# ]


data = [
  {
    "id": 1,
    "college_name": "Indian Institute of Technology Bombay",
    "courses": [
      {"course_name": "Computer Science and Engineering", "price": 200000, "enrollment": 300},
      {"course_name": "Electrical Engineering", "price": 180000, "enrollment": 250},
      {"course_name": "Mechanical Engineering", "price": 170000, "enrollment": 200}
    ],
    "employees": 800,
    "link": "https://www.iitb.ac.in/"
  },
  {
    "id": 2,
    "college_name": "Indian Institute of Science Bangalore",
    "courses": [
      {"course_name": "Aerospace Engineering", "price": 220000, "enrollment": 150},
      {"course_name": "Chemical Engineering", "price": 210000, "enrollment": 120},
      {"course_name": "Materials Science and Engineering", "price": 200000, "enrollment": 100}
    ],
    "employees": 700,
    "link": "https://iisc.ac.in/"
  },
  {
    "id": 3,
    "college_name": "Indian Institute of Technology Delhi",
    "courses": [
      {"course_name": "Civil Engineering", "price": 190000, "enrollment": 200},
      {"course_name": "Biotechnology", "price": 180000, "enrollment": 150},
      {"course_name": "Mathematics and Computing", "price": 200000, "enrollment": 180}
    ],
    "employees": 750,
    "link": "https://home.iitd.ac.in/"
  },
  {
    "id": 4,
    "college_name": "Indian Institute of Technology Kanpur",
    "courses": [
      {"course_name": "Aerospace Engineering", "price": 210000, "enrollment": 160},
      {"course_name": "Chemical Engineering", "price": 200000, "enrollment": 140},
      {"course_name": "Electrical Engineering", "price": 190000, "enrollment": 220}
    ],
    "employees": 650,
    "link": "https://www.iitk.ac.in/"
  },
  {
    "id": 5,
    "college_name": "Indian Institute of Technology Kharagpur",
    "courses": [
      {"course_name": "Computer Science and Engineering", "price": 200000, "enrollment": 300},
      {"course_name": "Mechanical Engineering", "price": 180000, "enrollment": 250},
      {"course_name": "Civil Engineering", "price": 170000, "enrollment": 200}
    ],
    "employees": 800,
    "link": "https://www.iitkgp.ac.in/"
  },
  {
    "id": 6,
    "college_name": "Indian Institute of Technology Madras",
    "courses": [
      {"course_name": "Electrical Engineering", "price": 200000, "enrollment": 250},
      {"course_name": "Computer Science and Engineering", "price": 220000, "enrollment": 300},
      {"course_name": "Mechanical Engineering", "price": 180000, "enrollment": 200}
    ],
    "employees": 850,
    "link": "https://www.iitm.ac.in/"
  },
  {
    "id": 7,
    "college_name": "Indian Institute of Technology Roorkee",
    "courses": [
      {"course_name": "Civil Engineering", "price": 190000, "enrollment": 200},
      {"course_name": "Biotechnology", "price": 180000, "enrollment": 150},
      {"course_name": "Mathematics and Computing", "price": 200000, "enrollment": 180}
    ],
    "employees": 700,
    "link": "https://www.iitr.ac.in/"
  },
  {
    "id": 8,
    "college_name": "Indian Institute of Technology Guwahati",
    "courses": [
      {"course_name": "Computer Science and Engineering", "price": 200000, "enrollment": 300},
      {"course_name": "Electronics and Communication Engineering", "price": 190000, "enrollment": 250},
      {"course_name": "Mechanical Engineering", "price": 180000, "enrollment": 200}
    ],
    "employees": 600,
    "link": "https://www.iitg.ac.in/"
  },
  {
    "id": 9,
    "college_name": "Birla Institute of Technology and Science, Pilani",
    "courses": [
      {"course_name": "Chemical Engineering", "price": 250000, "enrollment": 150},
      {"course_name": "Computer Science and Engineering", "price": 260000, "enrollment": 300},
      {"course_name": "Electrical and Electronics Engineering", "price": 240000, "enrollment": 200}
    ],
    "employees": 900,
    "link": "https://www.bits-pilani.ac.in/"
  },
  {
    "id": 10,
    "college_name": "National Institute of Technology Tiruchirappalli",
    "courses": [
      {"course_name": "Civil Engineering", "price": 180000, "enrollment": 200},
      {"course_name": "Computer Science and Engineering", "price": 200000, "enrollment": 300},
      {"course_name": "Mechanical Engineering", "price": 190000, "enrollment": 250}
    ],
    "employees": 700,
    "link": "https://www.nitt.edu/"
  }
]

conn = psycopg2.connect("dbname=1000xdev user=postgres password=pg123")
cur = conn.cursor()

for item in data:
    cur.execute(
        "INSERT INTO icolleges (college_name, courses, employees, link) VALUES (%s, %s, %s, %s)",
        (item["college_name"], json.dumps(item["courses"]), item["employees"], item["link"])
    )

conn.commit()
cur.close()
conn.close()
