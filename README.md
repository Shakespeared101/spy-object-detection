# Project Description: YOLO v7-Based Workplace Surveillance System

This project leverages the advanced capabilities of the YOLO v7 model and parallely processes 3 different YOLO v7 models for phone,camera and mirror detection respectively to enhance workplace security by detecting malicious recording and spying objects. The system is designed to identify potential threats such as mirrors, cameras, and phones placed near employee workstations. Additionally, it incorporates a face recognition module to monitor employee presence and detect any unauthorized individuals.

## Key Features

### Malicious Object Detection

- Utilizes the YOLO v7 model for real-time detection of spying devices.
- Identifies objects like mirrors, cameras, and phones that could be used for unauthorized recording or monitoring.
- Ensures that these objects are detected if they are placed in view of the employee’s workstation.

### Employee Presence Verification

- Integrates face recognition software to verify the identity of individuals at workstations.
- Detects whether an authorized employee is present and actively working.
- Identifies and alerts security personnel if an unknown person is observed near the workstation or looking at the monitor.

### Enhanced Security

- Provides a comprehensive solution to mitigate the risks of industrial espionage and privacy breaches.
- Helps maintain a secure and compliant workplace environment by preventing unauthorized surveillance.
- Can be integrated with existing security systems for real-time monitoring and alerting.

### Real-Time Monitoring

- Employs high-speed image processing to deliver real-time detection and recognition results.
- Ensures quick response times to potential security threats.

## Installation Instructions

To get started with the YOLO v7-based workplace surveillance system, follow these steps to clone the YOLO v7 repository, navigate to the directory, and install the necessary requirements:

1. Clone the YOLO v7 repository:
    ```bash
    !git clone https://github.com/WongKinYiu/yolov7
    ```

2. Change to the `yolov7` directory:
    ```bash
    %cd yolov7
    ```

3. Install the required dependencies:
    ```bash
    !pip install -r requirements.txt
    ```

## Obtaining Weight Files and Detect Scripts

To run the detection models for mirrors, cameras, and phones, you need the pre-trained weight files and the corresponding `detect.py` scripts. These files are not included in the repository by default. Please contact the repository owners or the project maintainers to obtain these files. You can reach out to them via the contact information provided on the repository page.

### Contacting the Owners

1. **Via GitHub Issues**:
    - Navigate to the [Issues](https://github.com/WongKinYiu/yolov7/issues) section of the repository.
    - Open a new issue and request access to the specific weight files and `detect.py` scripts.
    - Provide details about your use case and how you plan to use the weights.

2. **Via Email**:
    - If an email address is provided in the repository's contact information, send a request explaining your project and the files you need.
    - Be polite and detailed in your request to increase the chances of a positive response.

3. **Via GitHub Discussions**:
    - If the repository has a Discussions section, start a new discussion topic requesting the weight files and detect scripts.
    - Engage with the community and maintainers to explain your needs and collaborate.

Make sure to explain your project clearly and how the weight files and `detect.py` scripts will be used to ensure a smooth and positive interaction with the repository owners.

Contributors:
* Aditya Sai SD
* B Shakthi
