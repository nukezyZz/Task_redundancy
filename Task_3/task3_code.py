import datetime
import random

def generate_bus_pass():
    print("\n--- Cloud Bus Pass Generator ---")

    name = input("Enter your name: ").strip()
    age = input("Enter your age: ").strip()
    route = input("Enter bus route number: ").strip()
    duration = input("Pass Duration (Daily/Weekly/Monthly): ").strip()
    unique_id = input("Enter unique ID number: ").strip()

    # basic validation
    if not (name and age.isdigit() and route and duration and unique_id):
        print("\nError: Invalid input. All fields must be filled correctly.")
        return

    # generate validity date
    today = datetime.date.today()
    if duration.lower() == "daily":
        valid_upto = today + datetime.timedelta(days=1)
    elif duration.lower() == "weekly":
        valid_upto = today + datetime.timedelta(days=7)
    else:
        valid_upto = today + datetime.timedelta(days=30)

    # generate QR-style random code
    qr_code = random.randint(100000, 999999)

    pass_html = f"""
    <html>
    <head>
        <title>Bus Pass</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                padding: 20px;
            }}
            .card {{
                width: 300px;
                padding: 20px;
                border: 2px solid #333;
                border-radius: 10px;
            }}
            .photo {{
                width: 80px;
                height: 80px;
                background: #ccc;
                border-radius: 10px;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h2>Bus Pass</h2>
            <div class="photo"></div>
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Age:</strong> {age}</p>
            <p><strong>Route:</strong> {route}</p>
            <p><strong>Duration:</strong> {duration}</p>
            <p><strong>ID:</strong> {unique_id}</p>
            <p><strong>Valid Until:</strong> {valid_upto}</p>
            <p><strong>QR Code:</strong> {qr_code}</p>
        </div>
    </body>
    </html>
    """

    with open("bus_pass_output.html", "w") as file:
        file.write(pass_html)

    print("\nBus pass generated successfully! Check 'bus_pass_output.html'")

generate_bus_pass()
