import streamlit as st
import tensorflow as tf
from tensorflow.keras.utils import load_img, img_to_array
import numpy as np

# -----------------------------
# PAGE SETTINGS 
# -----------------------------

st.set_page_config(
    page_title="RecycleScan",
    page_icon="♻️",
    layout="centered"
)

# -----------------------------
# CUSTOM UI
# -----------------------------

st.markdown("""
<style>

.block-container {
    max-width: 700px;
    padding-top: 2rem;
    padding-left: 1rem;
    padding-right: 1rem;
}

.title {
    text-align: center;
    font-size: 38px;
    font-weight: 800;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 16px;
    margin-bottom: 25px;
}

.section-title {
    font-size: 22px;
    font-weight: 700;
    margin-top: 25px;
    margin-bottom: 12px;
}

.result-box {
    border: 1px solid rgba(128,128,128,0.35);
    border-radius: 16px;
    padding: 22px;
    margin-top: 20px;
    text-align: center;
}

.result-title {
    font-size: 30px;
    font-weight: 800;
    margin-bottom: 5px;
}

.score {
    font-size: 19px;
    font-weight: 600;
}

.recommendation-box {
    border: 1px solid rgba(128,128,128,0.35);
    border-radius: 16px;
    padding: 20px;
    margin-top: 18px;
}

.recommendation-text {
    font-size: 16px;
    line-height: 1.6;
}

.footer {
    text-align: center;
    margin-top: 35px;
    margin-bottom: 15px;
    font-size: 14px;
    line-height: 1.6;
}

@media (max-width: 600px) {

    .block-container {
        padding-top: 1.2rem;
        padding-left: 0.8rem;
        padding-right: 0.8rem;
    }

    .title {
        font-size: 32px;
    }

    .subtitle {
        font-size: 15px;
    }

    .result-title {
        font-size: 27px;
    }

    .score {
        font-size: 18px;
    }

    .recommendation-text {
        font-size: 15px;
    }

}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------

st.markdown(
    '<div class="title">♻️ RecycleScan</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI-Powered Waste Identification</div>',
    unsafe_allow_html=True
)

st.write(
    "Upload a photo of a waste item and RecycleScan will "
    "identify its category and suggest the appropriate disposal method."
)

# -----------------------------
# LOAD BALANCED MODEL
# -----------------------------

@st.cache_resource
def load_model():
    return tf.keras.models.load_model(
        "recyclescan_balanced_model.keras"
    )

model = load_model()

# -----------------------------
# CLASSES
# -----------------------------

class_names = [
    "cardboard",
    "e_waste",
    "glass",
    "metal",
    "organic",
    "paper",
    "plastic",
    "shoes",
    "textile",
    "trash"
]

# -----------------------------
# RECOMMENDATIONS
# -----------------------------

recommendations = {

    "cardboard":
        "Flatten clean cardboard and place it in the paper/cardboard recycling bin.",

    "e_waste":
        "Do not throw e-waste in regular bins. Give it to an authorized e-waste recycling center.",

    "glass":
        "Handle glass carefully and place it in a designated glass recycling container.",

    "metal":
        "Clean the metal item and place it in a metal recycling bin.",

    "organic":
        "Place organic waste in a composting or wet-waste collection bin.",

    "paper":
        "Keep paper clean and dry, then place it in the paper recycling bin.",

    "plastic":
        "Clean the plastic item and place it in a recyclable waste bin. Avoid burning plastic.",

    "shoes":
        "If usable, donate or reuse the shoes. Damaged footwear can be given to an appropriate textile or footwear collection facility.",

    "textile":
        "Reuse or donate usable textiles. Damaged fabric and clothing can be given to a textile recycling or collection facility.",

    "trash":
        "Place general non-recyclable waste in the appropriate general-waste bin."
}

# -----------------------------
# UPLOAD IMAGE
# -----------------------------

st.markdown(
    '<div class="section-title">📷 Upload Waste Image</div>',
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"],
    help="Upload a clear photo of the waste item."
)

# -----------------------------
# PREDICTION
# -----------------------------

if uploaded_file is not None:

    st.image(
        uploaded_file,
        caption="Uploaded Waste Image",
        width="stretch"
    )

    with st.spinner("🔍 Analyzing image..."):

        # Load image
        image = load_img(
            uploaded_file,
            target_size=(224, 224)
        )

        image_array = img_to_array(image)

        image_array = np.expand_dims(
            image_array,
            axis=0
        )

        # Make prediction
        prediction = model.predict(
            image_array,
            verbose=0
        )[0]

        # Get top 3 predictions
        top_3 = np.argsort(prediction)[-3:][::-1]

        predicted_index = top_3[0]

        predicted_class = class_names[
            predicted_index
        ]

        score = prediction[
            predicted_index
        ] * 100

    display_name = (
        predicted_class
        .replace("_", " ")
        .title()
    )

    # -----------------------------
    # AI ANALYSIS
    # -----------------------------

    st.markdown(
        '<div class="section-title">🔍 AI Analysis</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="result-box">
            <div class="result-title">{display_name}</div>
            <div class="score">Confidence: {score:.2f}%</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.progress(
        min(int(score), 100)
    )

    # -----------------------------
    # CONFIDENCE MESSAGE
    # -----------------------------

    if score < 50:

        st.warning(
            "⚠️ The model is uncertain about this prediction. "
            "Try uploading a clearer photo with the waste item "
            "more visible."
        )

    elif score < 70:

        st.info(
            "ℹ️ The model has moderate confidence. "
            "A clearer image may improve the prediction."
        )

    else:

        st.success(
            "✅ The model has a strong prediction for this image."
        )

    # -----------------------------
    # TOP 3 PREDICTIONS
    # -----------------------------

    st.markdown(
        '<div class="section-title">📊 Top 3 Predictions</div>',
        unsafe_allow_html=True
    )

    for index in top_3:

        name = (
            class_names[index]
            .replace("_", " ")
            .title()
        )

        confidence = prediction[index] * 100

        st.write(
            f"**{name}** — {confidence:.2f}%"
        )

        st.progress(
            min(int(confidence), 100)
        )

    # -----------------------------
    # RECOMMENDATION
    # -----------------------------

    st.markdown(
        '<div class="section-title">💡 Disposal Recommendation</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="recommendation-box">
            <div class="recommendation-text">
                {recommendations[predicted_class]}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# -----------------------------
# SUPPORTED CATEGORIES
# -----------------------------

with st.expander("♻️ Supported Waste Categories"):

    categories = [
        "📦 Cardboard",
        "🔌 E-Waste",
        "🍾 Glass",
        "🔩 Metal",
        "🌱 Organic",
        "📄 Paper",
        "🧴 Plastic",
        "👟 Shoes",
        "👕 Textile",
        "🗑️ General Trash"
    ]

    for category in categories:
        st.write(category)

# -----------------------------
# FOOTER
# -----------------------------

st.markdown(
    """
    <div class="footer">
        ♻️ RecycleScan<br>
        <b>Identify Waste. Sort Smart. Recycle Better.</b>
    </div>
    """,
    unsafe_allow_html=True
)
