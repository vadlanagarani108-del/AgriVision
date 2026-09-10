from PIL import Image


def analyze_crop_image(image_path):
    """
    Demo-ready local crop screening.
    Placeholder until a trained ML model is connected.
    """

    try:
        image = Image.open(image_path)

        if image.width < 100 or image.height < 100:
            return {
                "crop_name": "Image too small",
                "health_status": "Unable to analyze",
                "possible_disease": "Please upload a clearer image",
                "care_advice": "Use a clear crop or leaf photograph.",
                "confidence": 0,
            }

        return {
            "crop_name": "Crop detected",
            "health_status": "Healthy - preliminary screening",
            "possible_disease": "No visible disease detected",
            "care_advice": (
                "Continue regular watering and monitor the crop "
                "for changes in leaf color, spots, or pest activity."
            ),
            "confidence": 85,
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