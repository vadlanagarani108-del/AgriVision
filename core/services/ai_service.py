from PIL import Image
import os


def analyze_crop_image(image_path):
    """
    Temporary local crop screening.
    Real ML model will be connected after the core workflow is stable.
    """

    try:
        image = Image.open(image_path)

        # Basic validation
        if image.width < 100 or image.height < 100:
            return {
                "crop_name": "Image too small",
                "health_status": "Unable to analyze",
                "possible_disease": "Please upload a clearer image",
                "care_advice": "Use a clear crop or leaf photograph.",
                "confidence": 0,
            }

        return {
            "crop_name": "Crop image received",
            "health_status": "Ready for AI screening",
            "possible_disease": "AI model pending",
            "care_advice": (
                "Image uploaded successfully. "
                "The crop should be inspected with a trained "
                "agriculture AI model before treatment decisions."
            ),
            "confidence": 0,
        }

    except Exception as error:
        print("Image Error:", error)

        return {
            "crop_name": "Analysis unavailable",
            "health_status": "Unable to analyze",
            "possible_disease": "Please try another image",
            "care_advice": "Upload a clear crop image and try again.",
            "confidence": 0,
        }