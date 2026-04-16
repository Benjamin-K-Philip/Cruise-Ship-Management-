# Cruise Ship Management

## Description
Costas Cruise Ship Management is a Python-based software solution designed to enhance the operational efficiency of cruise ship hotels. It provides a unified interface for passengers to manage their entire cruise experience, from initial booking to onboard services. The project aims to simplify complex processes by allowing passengers to make reservations for rooms, restaurants, and wellness facilities effortlessly while maintaining a comprehensive record of all their plans

---

## How the Code Works

The application is built using modular programming principles, where functionality is divided into various reusable components to ensure a structured and efficient codebase.

➤ Core Architecture and Modules <br>
The system is organized into several key components that handle different functional domains: <br>

   - Booking and Reservation Modules: Modules like bookin and book handle passenger details (name, address, phone) and destination selection (e.g., Egypt, Jordan, or Madagascar).

   - Service and Information Modules: Specific modules such as OCRiveria, Arcrink, and med provide detailed information about cruise facilities through a centralized reception system.

   - Facility Management Modules: A vast array of imported modules (e.g., nuska, bastion, fika) manage individual restaurant descriptions, time slot availability, and booking logic.

   - Error Handling Modules: Specialized modules like bookerrors, roomerrors, and nuskatimeerrors are used to manage invalid user inputs and provide second attempts for data entry.

➤ Core Logic and Flow



Passenger Registration: The bookin() function captures user identity and contact information.



Selection and Pricing: The book() function opens external text files to display destination options and uses conditional logic to set prices and room types (Regular or Premium).

Data Persistence: Reservations are recorded in structured formats. For example, room bookings are appended to room_booking.csv using the csv.writer module, while restaurant bookings are saved to both .txt and .csv files.



Interactive Loops: The reception() and facilities() functions use while loops and try-except blocks to allow passengers to navigate through different onboard options without restarting the program.

➤ Implementation of Packages and Tools



Standard Python Packages: import random is used for assigning seat numbers, import time creates realistic delays for print statements, and import csv manages structured data exchange.

Custom Modules (Packages): The project relies heavily on user-defined modules to keep the main program clean. Each feature (like a specific restaurant or error type) is isolated in its own file and brought in via import statements.



File I/O: The code uses Python’s built-in open() function with various modes ('r' for reading descriptions, 'a' or 'a+' for appending new bookings) to manage persistent data across sessions.
