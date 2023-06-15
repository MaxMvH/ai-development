import os
import streamlit as st
import vertexai
from vertexai.preview.language_models import TextGenerationModel
from PIL import Image

# Initialize color
COLOR = '#4081e3' 

def predict_large_language_model_sample(
    project_id: str,
    model_name: str,
    temperature: float,
    max_decode_steps: int,
    top_p: float,
    top_k: int,
    content: str,
    location: str = "us-central1",
    tuned_model_name: str = "",
    ) :
    """Predict using a Large Language Model."""
    vertexai.init(project=project_id, location=location)
    model = TextGenerationModel.from_pretrained(model_name)
    if tuned_model_name:
        model = model.get_tuned_model(tuned_model_name)
    response = model.predict(
        content,
        temperature=temperature,
        max_output_tokens=max_decode_steps,
        top_k=top_k,
        top_p=top_p,)
    return response.text

# Use the full page instead of a narrow central column
st.set_page_config(layout="wide")

st.markdown(f"<h1 style='text-align: center; color: {COLOR};'>Automate Marketing Content Creation - Category Descriptions</h1>", unsafe_allow_html=True)

# Add image at the top of the dashboard
image = Image.open('../utils/mvhmedia.jpg')  
st.image(image, use_column_width=True)

# Collecting user inputs
st.markdown(f"<h2 style='text-align: left; color: {COLOR};'>Enter the following details:</h2>", unsafe_allow_html=True)

st.markdown("#### **Category name**")
st.markdown("This is the main category for which you are creating the description.")
category_name = st.text_input("")

st.markdown("#### **Keywords**")
st.markdown("Enter the relevant keywords for your category (separated by commas). These will be used to generate the description.")
keywords = st.text_input("", key='keywords')

st.markdown("#### **Company**")
st.markdown("Enter your company's name as you'd like it to appear in the description.")
company = st.text_input("", key='company')

# When the 'Generate Description' button is clicked, call the LLM function
if st.button('Generate Description'):
    st.markdown(f"<h2 style='text-align: left; color: {COLOR};'>Generated Description</h2>", unsafe_allow_html=True)

    specific_prompt = f'''Background: When it comes to SEO for e-commerce sites, optimising category pages (a.k.a product listing pages) is key for success. Categories are some of the most authoritative pages on a site because they are linked from the navigation and link out to important assets like products. With their high level of authority, they can be much more effective at driving organic traffic than other pages like products. Some key insights for great category descriptions are providing useful and quality content, exhausting the topic, ensuring readability, adequately promoting your products.

    Here are more detailed information about important aspects to take into account while writing a category description:
    - Purpose: An SEO category description provides information about the products that are helpful for shoppers and includes relevant keywords. It features on e-commerce category pages and can be placed at the top or bottom of these pages​​.
    - Optimization: One effective way to optimise category pages for SEO is to include a well-written category description. Additional content provides search engines with better context about the relevant keywords for your page​.
    - Benefits: Well-optimised category descriptions can greatly improve the ranking of product listing pages, increase visibility for more keywords, and drive more organic search traffic​.
    - User-Centric: The content should be created for users, not just for search engines. It should provide important, relevant information about your products that is helpful for both users and search engines​​.
    - Product Highlights: The category description should act as an elevator pitch for your products. It should provide information about the products\' uses, benefits, and types (styles, brands, colors, etc.) to clearly convey why your products are suitable for shoppers​​.
    - Brand Voice: The descriptions should align with your brand voice for consistency across your site. Understanding your audience is crucial in establishing a good brand voice​.
    - Keywords: Relevant keywords, long-tail keywords, keyword variants, and semantic keywords should be included in the category description to target a variety of new keywords.


    Your task: You will act as an Search Engine Optimization (SEO) expert that works for a Dutch Online Marketing Agency. You will write SEO optimised category descriptions for product categories based on keywords that will be provided to you. The category description should be at least 500 characters long, ideally around 1000 characters.

    input: Category name: White Nike Shoes
    Keywords: footwear, shoes, nike, quality
    Company: Kohl


    output: WHITE NIKE SHOES
    As one of the most recognizable brands on the planet, Nike has become a trailblazing powerhouse in the world of athletic apparel and accessories, and it all started with their line of athletic shoes. And when it comes to eye-catching, ultra comfortable white Nike shoes, no one carries a wider selection than Kohl\'s! 
    While Nike shoes are renowned for their unparalleled quality and superior performance in the world of sport, they\'ve also become an iconic casual fashion accessory that can enhance just about any outfit. 

    input: Category name: Televisions
    Keywords: screen, TV, HD, image
    Company: Expert.nl
    output: Televisions
    Do you want to buy a new TV? At Expert you will find a full range of televisions from all major TV brands. There are TVs for sale in different screen formats. Choose a Smart TV to watch online content, such as YouTube and Netflix. There are TVs with different image technologies, such as QLED, OLED or Ambilight. Do you like to watch movies or football matches in the best image quality? Then view our 4K Ultra HD Televisions or 8K Ultra HD Televisions. Would you like to know which TV suits your needs? 

    input: Category name: Samsung TVs
    Keywords: Samsung, screen, TV, QLED, image
    Company: Expert.nl
    output: Samsung TVs
    Beautiful image with a Samsung TV
    Are you looking for a new TV? Then a Samsung TV is an excellent choice. Samsung TVs produce a beautiful image in a beautiful design. The top models of Samsung TVs are the Samsung QLED TVs , televisions with a screen made up of millions of crystals that provide beautiful clarity and lifelike colors. Are you looking for the sharpest image? You can also buy a Samsung TV. Samsung has QLED 8K TVs in its range, TVs that are another 4 times as sharp as the already super-sharp QLED 4K TVs. With this you don\'t have to miss a single detail anymore.

    input: Category name: PC Speakers
    Keywords: Sound, computer, speaker
    Company: Expert.nl
    output: PC Speakers
    Good sound is so nice if you are gaming on your computer or want to watch the latest YouTube videos. This is not possible with the standard speakers that are built into computers and laptops. Buying a speaker set for the PC offers a solution. At Expert you buy the PC speakers that best suit your sound needs. See our range below and see which PC speaker you prefer to purchase. Buy the PC speakers directly online or come to one of our 140 stores for a demonstration.

    input: Category name: Household & Living
    Keywords: House, clean, devices
    Company: Expert.nl
    output: Household & Living
    Are you looking for a solution to easily and quickly clean the house or to smooth out your clothes? Expert has a wide range of vacuum cleaners, irons and cleaning devices to get that done. At Expert you will find everything for your home. Washing machines and dryers for wonderfully clean clothes, heaters for the cold winter days and air conditioners and fans for the summer. Expert is also the right place for lighting or a baby monitor. And then there are the Smart Home devices that make life easy. Discover our wide range on Expert.nl, or visit one of our 140 Expert stores and receive personal advice.

    input: Category name: Hair styling
    Keywords: Brush, dryer, hair, curls
    Company: Expert.nl
    output: Hair styling
    Want to buy a hair straightener, curling iron, curling brush or hair dryer? With the extensive range of hair styling products you can go in any direction with your hair. You can easily create a straight haircut with a wide hair straightener or a bunch of curls with a curling iron. Due to the different temperature settings, we have the right device for every type of hair. View and buy your styling product on Expert.nl. Would you prefer more advice first? Then come to one of our 140 stores . Our Experts are happy to help you!

    input: Category name: Phones and tablets
    Keywords: Phones, tablets, iPhone, Android, mobile, smartphone
    Company: Expert.nl
    output: Phones and tablets
    With the  phones  and  tablets  that you buy from Expert, calling family, texting friends and/or slumped on the couch online booking a holiday or picking out new clothes is no problem. Buy a smartphone , such as an iPhone or an Android phone if you not only want to make calls, but also want to be active online. You buy a DECT telephone to be accessible in and around the house. A tablet is light, compact and easy to operate (one finger is enough). Don\'t need all the modern bells and whistles? Then buy a mobile phone. In this category you can also choose from our wearables and navigation systems and you will find accessories for your smartphone such as power banks , chargers, charging cables, phone cases and screen protectors. See our wide range of phones and tablets below and discover what suits you best. Buy your phone and/or tablet directly online or come to one of our 140 stores for a demonstration!

    input: Category name: {category_name}
    Keywords: {keywords}
    Company: {company}
    output:
    '''

    global_prompt = specific_prompt

    generated_text = predict_large_language_model_sample(
        "mvhmedia", 
        "text-bison@001", 
        0.2, 
        1024, 
        0.95, 
        40, 
        global_prompt, 
        "us-central1"
    )
    
    st.markdown(generated_text, unsafe_allow_html=True)
