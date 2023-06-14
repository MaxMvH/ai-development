# Automate Marketing Content Creation with AI

Welcome to the *Automate Marketing Content Creation - Category Descriptions* project! This project aims to help marketing teams generate SEO-optimized descriptions for their e-commerce product categories, significantly reducing the time it takes to write these descriptions manually and ensuring the descriptions are optimized for SEO. This application uses Google's Vertex AI's language model to generate the descriptions based on given keywords.

This project is built with [Streamlit](https://streamlit.io/), a powerful platform for building data apps quickly, and [Vertex AI](https://cloud.google.com/vertex-ai), a managed machine learning platform that allows developers and data scientists to build, deploy, and scale AI models faster.

## Project Structure

- `ai-development`
  - `src`
    - `app.py`: The main application file which runs the Streamlit app.
  - `utils`
    - `creds.json`: Google Cloud service account credentials file.

## How It Works

The application takes the following inputs from the user:

- `Category name`: The name of the product category for which you want to generate a description.
- `Keywords`: Relevant keywords related to the product category, separated by commas.
- `Company`: The name of your company.

Once you input these details and click on the 'Generate Description' button, the application will generate a SEO-optimized description for the product category.

## Installation

To run the application on your local machine, follow these steps:

1. Install the required Python packages: `pip install streamlit vertexai`

2. Clone this repository.

3. Navigate to the project directory: `cd ai-development/src`

4. Run the Streamlit app: `streamlit run app.py`

5. A local URL will be displayed in your terminal. Open this URL in your web browser to interact with the application.

## Deployment on Google Cloud Platform

This application can be deployed on a Google Cloud Platform (GCP) Virtual Machine (VM) for wider access. To do this, you will need to set up a GCP account and install the Google Cloud SDK. Please refer to the GCP documentation for detailed steps.

---

Please note that while this application aims to provide SEO-optimized descriptions, the results should be reviewed and potentially edited to better match your specific SEO strategy. Use this tool as a way to get started with your descriptions and reduce the amount of time it takes to create them.
