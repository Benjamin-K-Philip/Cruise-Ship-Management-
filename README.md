# Cruise Ship Management

## Description
Costas Cruise Ship Management is a Python-based software solution designed to enhance the operational efficiency of cruise ship hotels. It provides a unified interface for passengers to manage their entire cruise experience, from initial booking to onboard services. The project aims to simplify complex processes by allowing passengers to make reservations for rooms, restaurants, and wellness facilities effortlessly while maintaining a comprehensive record of all their plans

---

## How the Code Works

The application is built using modular programming principles, where functionality is divided into various reusable components to ensure a structured and efficient codebase.

➤ **Core Architecture and Modules** <br>
The system is organized into several key components that handle different functional domains: <br>

   - **Booking and Reservation Modules:** Modules like bookin and book handle passenger details (name, address, phone) and destination selection (e.g., Egypt, Jordan, or Madagascar).

   - **Service and Information Modules:** Specific modules such as OCRiveria, Arcrink, and med provide detailed information about cruise facilities through a centralized reception system.

   - **Facility Management Modules:** A vast array of imported modules (e.g., nuska, bastion, fika) manage individual restaurant descriptions, time slot availability, and booking logic.

   - **Error Handling Modules:** Specialized modules like bookerrors, roomerrors, and nuskatimeerrors are used to manage invalid user inputs and provide second attempts for data entry.

     
➤ **Core Logic and Flow** <br>
   - **Passenger Registration:** The bookin() function captures user identity and contact information.

   - **Selection and Pricing:** The book() function opens external text files to display destination options and uses conditional logic to set prices and room types (Regular or Premium).

   - **Data Persistence:** Reservations are recorded in structured formats. For example, room bookings are appended to room_booking.csv using the csv.writer module, while restaurant  bookings are saved to both .txt and .csv files.

   - **Interactive Loops:** The reception() and facilities() functions use while loops and try-except blocks to allow passengers to navigate through different onboard options without restarting the program.


➤ **Implementation of Packages and Tools** <br>
   - **Standard Python Packages:** import random is used for assigning seat numbers, import time creates realistic delays for print statements, and import csv manages structured data exchange.

   - **Custom Modules (Packages):** The project relies heavily on user-defined modules to keep the main program clean. Each feature (like a specific restaurant or error type) is isolated in its own file and brought in via import statements.

   - **File I/O:** The code uses Python’s built-in open() function with various modes ('r' for reading descriptions, 'a' or 'a+' for appending new bookings) to manage persistent data across sessions.

---


## Features <br>
  - **Cruise Package Selection:** Offers three distinct cruise packages with different destinations and budget options.

  - **Cabin Customization:** Passengers can choose between Regular and Premium suites, with automated room number generation.

  - **Table Booking System:** An interactive feature for reserving tables at signature dining venues like Nuska Beach or Bastion, including specific time slots for breakfast, lunch, or dinner.

  - **Onboard Facilities Exploration:** Detailed guides for pools, spas, fitness centers, arcades, and even specialized menus (e.g., Jain, Kosher, or Vegan meals).

  - **Activity Pre-booking:** Allows users to reserve spots for onboard entertainment and sports activities.

---


## Project Structure <br>
The project is organized into functional categories to maintain a clean directory: <br>

**Main Logic:** The primary source code file containing the main execution flow and function definitions.

**Information Files:** Text files (e.g., receptiontext.txt, factext.txt) that store the descriptive content shown to the user.

**Data Storage:** CSV and TXT files (e.g., room_booking.csv, nuska.txt) that act as a database for passenger reservations.

**Feature Modules:** Individual .py files for every facility (like OCRiveria.py) and error handling (like roombkerrors.py)

---


## Output 
<img width="1253" height="667" alt="image" src="https://github.com/user-attachments/assets/a5392b26-eaa0-431d-af5f-f87b261b8db7" />

<img width="1242" height="442" alt="image" src="https://github.com/user-attachments/assets/cec085b1-ebec-45cb-be92-1a58b546ed4d" />

<img width="1233" height="509" alt="image" src="https://github.com/user-attachments/assets/4906489e-474d-4de1-aa82-314cbe029d1a" />

<img width="1247" height="620" alt="image" src="https://github.com/user-attachments/assets/f9b320d5-c27e-444b-818a-728507b75d05" />

<img width="1249" height="448" alt="image" src="https://github.com/user-attachments/assets/7fe7d083-6ca3-455a-b2e5-07b29ef1354d" />

<img width="1327" height="527" alt="image" src="https://github.com/user-attachments/assets/84c3f85c-c6e6-4016-bbc3-bc4276dbce98" />

<img width="1259" height="636" alt="image" src="https://github.com/user-attachments/assets/27bca647-09cb-4858-bcf6-9c0acc8f0e76" />

<img width="1232" height="452" alt="image" src="https://github.com/user-attachments/assets/f53c07b5-920e-498a-8c66-b6f514bf3466" />

<img width="1294" height="651" alt="image" src="https://github.com/user-attachments/assets/e33a5d86-0b13-4148-884c-1c8cf1c4075c" />

<img width="1275" height="517" alt="image" src="https://github.com/user-attachments/assets/a1119fbb-6837-4d71-981a-960d3920c427" />

<img width="1272" height="611" alt="image" src="https://github.com/user-attachments/assets/890645e1-8a60-41cd-91ab-79e2aa1b8f9d" />

<img width="1264" height="611" alt="image" src="https://github.com/user-attachments/assets/8304368a-0b02-4f77-86f8-a40c075bbfa2" />

<img width="1270" height="608" alt="image" src="https://github.com/user-attachments/assets/482ea4e9-ea4b-47f7-9c4c-8ce8b4937000" />

<img width="1278" height="535" alt="image" src="https://github.com/user-attachments/assets/4323f980-17e1-4f8e-a564-60a12b8ea41a" />

<img width="1282" height="562" alt="image" src="https://github.com/user-attachments/assets/29bbd665-1b3b-40f5-90b1-7f2645c31f63" />

<img width="1277" height="560" alt="image" src="https://github.com/user-attachments/assets/cf8d00e9-b8c9-40d9-8436-0f19984de8a0" />

<img width="1292" height="617" alt="image" src="https://github.com/user-attachments/assets/60c851e9-b686-4dac-ad03-7d1115aaf60c" />

<img width="1323" height="569" alt="image" src="https://github.com/user-attachments/assets/efa98987-9f96-4184-bbcb-fe698d164b50" />

<img width="1317" height="259" alt="image" src="https://github.com/user-attachments/assets/1df304d4-1686-4e92-a267-f75bec4491a0" />

<img width="1271" height="651" alt="image" src="https://github.com/user-attachments/assets/c963b3c0-5727-4956-a2a4-3351f2421268" />

<img width="1271" height="505" alt="image" src="https://github.com/user-attachments/assets/e0d99107-f01b-4c25-b878-8d97b1fc7a85" />

<img width="1333" height="610" alt="image" src="https://github.com/user-attachments/assets/25d62461-8d19-432c-ac91-c60891951dda" />

<img width="1313" height="458" alt="image" src="https://github.com/user-attachments/assets/39165387-91f0-48c5-b318-20e94dfed8e2" />

<img width="1334" height="354" alt="image" src="https://github.com/user-attachments/assets/49d2c64f-dc79-4fb6-9b81-84afb77af23d" />

<img width="1305" height="393" alt="image" src="https://github.com/user-attachments/assets/0c9d23db-50dc-469c-9958-b55afbac5d5c" />

<img width="1338" height="318" alt="image" src="https://github.com/user-attachments/assets/c0c17d1a-aaa6-4ee7-9a6c-357021524a83" />

<img width="1317" height="359" alt="image" src="https://github.com/user-attachments/assets/bf3c737d-eae0-4e4c-914f-d8e6f0a9c580" />

<img width="1273" height="646" alt="image" src="https://github.com/user-attachments/assets/e9db1963-573d-4e38-89a6-ba61e8e126bf" />

<img width="1311" height="470" alt="image" src="https://github.com/user-attachments/assets/6d39c08c-d3f0-4b2a-9c00-81574a616704" />

<img width="1280" height="605" alt="image" src="https://github.com/user-attachments/assets/3efa7232-a351-47e2-b683-c0d372e88bb0" />

<img width="1320" height="258" alt="image" src="https://github.com/user-attachments/assets/b04e6297-19af-4398-b270-63af2a0ecb5d" />

<img width="1287" height="501" alt="image" src="https://github.com/user-attachments/assets/504fc285-c1d5-46ff-ab75-401183bb01c3" />

<img width="1303" height="537" alt="image" src="https://github.com/user-attachments/assets/bf315481-ac77-4544-b172-421dced4ca18" />

<img width="1283" height="611" alt="image" src="https://github.com/user-attachments/assets/5d07d821-b39d-4b3f-afb6-49432cb824b8" />

<img width="1345" height="404" alt="image" src="https://github.com/user-attachments/assets/bd2d52ea-820e-4b4f-b9fa-bf4eeb1d4506" />

--- 

## Output - CSV Files Genreated (i.e. Excel Files)
<img width="1366" height="727" alt="image" src="https://github.com/user-attachments/assets/557a97d4-dc5a-4e1b-a89b-777f10717a65" />

<img width="1366" height="728" alt="image" src="https://github.com/user-attachments/assets/f60301d5-84e3-48e8-be98-381c6f6cdf8c" />

<img width="1366" height="725" alt="image" src="https://github.com/user-attachments/assets/38ae33f2-a342-48a8-9cff-ff12deb1cd09" />

<img width="1366" height="727" alt="image" src="https://github.com/user-attachments/assets/cce4c687-5369-4556-84e8-e4f5a579546f" />

<img width="1366" height="723" alt="image" src="https://github.com/user-attachments/assets/be7a9ec0-66e0-44ed-bfb4-525a7281abce" />

<img width="1366" height="727" alt="image" src="https://github.com/user-attachments/assets/7faaa438-8e03-43db-9476-51f645f11972" />

<img width="1366" height="727" alt="image" src="https://github.com/user-attachments/assets/bb4d80e2-7fb9-4909-b662-6a2c148ac67d" />

 <img width="1366" height="727" alt="image" src="https://github.com/user-attachments/assets/28f7e1d9-0fa7-4b81-b7f5-f0889041559a" />


---


## Note:<br>
**Step-by-Step Instructions on how to run the given project:** <br>

1.**Download** the zip folder named **1-Refer this-Cruise Ship Management Source Code.zip.**

2.**Extract** the entire folder into a single directory on your computer.

3.Make sure all the **extracted files are in the same folder**.

4.**Run the main file, i.e., Cruise Ship Management Source Code.py.** (Note: The code must be extracted first so Python can access all the interconnected modules and data files).
