# Smart Product Recommendation Agent
# -----------------------------------
# Requirements:
# pip install openai pandas

import os
import pandas as pd
from openai import OpenAI

# -----------------------------
# 1. Product Database
# -----------------------------

products = pd.DataFrame([
    {
        "name": "iPhone 15",
        "category": "mobile",
        "price": 60000,
        "rating": 4.7,
        "features": "Excellent camera, fast processor, premium design"
    },
    {
        "name": "Samsung Galaxy S24",
        "category": "mobile",
        "price": 70000,
        "rating": 4.6,
        "features": "AMOLED display, excellent camera, powerful processor"
    },
    {
        "name": "OnePlus 12",
        "category": "mobile",
        "price": 50000,
        "rating": 4.5,
        "features": "Fast charging, powerful performance, good camera"
    },
    {
        "name": "MacBook Air M3",
        "category": "laptop",
        "price": 90000,
        "rating": 4.8,
        "features": "M3 chip, lightweight, long battery life"
    },
    {
        "name": "Dell Inspiron",
        "category": "laptop",
        "price": 65000,
        "rating": 4.4,
        "features": "Intel processor, 16GB RAM, good for students"
    },
    {
        "name": "HP Pavilion",
        "category": "laptop",
        "price": 55000,
        "rating": 4.3,
        "features": "Good performance, 16GB RAM, SSD storage"
    },
    {
        "name": "Sony WH-1000XM5",
        "category": "headphones",
        "price": 30000,
        "rating": 4.8,
        "features": "Excellent noise cancellation, premium sound"
    },
    {
        "name": "JBL Tune 770NC",
        "category": "headphones",
        "price": 7000,
        "rating": 4.4,
        "features": "Noise cancellation, strong bass, long battery"
    }
])

# -----------------------------
# 2. Recommendation Function
# -----------------------------

def recommend_products(category, budget, preference=""):
    data = products[
        (products["category"].str.lower() == category.lower()) &
        (products["price"] <= budget)
    ].copy()

    if data.empty:
        return data

    # Preference-based scoring
    preference_words = preference.lower().split()

    def calculate_score(row):
        score = row["rating"] * 10

        for word in preference_words:
            if word in row["features"].lower():
                score += 5

        return score

    data["score"] = data.apply(calculate_score, axis=1)

    return data.sort_values(
        by="score",
        ascending=False
    ).head(3)


# -----------------------------
# 3. AI Explanation
# -----------------------------

def generate_ai_response(user_query, recommendations):

    if recommendations.empty:
        return "Sorry, I could not find a product matching your requirements."

    product_info = "\n".join(
        f"{row['name']} - ₹{row['price']} - "
        f"Rating: {row['rating']} - {row['features']}"
        for _, row in recommendations.iterrows()
    )

    prompt = f"""
You are a smart product recommendation agent.

User request:
{user_query}

Recommended products:
{product_info}

Explain which product is the best choice for the user.
Compare the products briefly.
Give a simple and useful recommendation.
"""

    try:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful product recommendation assistant."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content

    except Exception:
        return "AI explanation unavailable. Showing product recommendations."


# -----------------------------
# 4. Smart Recommendation Agent
# -----------------------------

def recommendation_agent():

    print("\n===================================")
    print("   SMART PRODUCT RECOMMENDATION")
    print("===================================")

    print("\nAvailable categories:")
    print("mobile")
    print("laptop")
    print("headphones")

    category = input("\nWhat product are you looking for? ")
    budget = float(input("What is your maximum budget? ₹"))
    preference = input(
        "What is important to you? "
        "(camera/performance/battery/sound/etc.): "
    )

    user_query = (
        f"I need a {category} under ₹{budget}. "
        f"My preference is {preference}."
    )

    recommendations = recommend_products(
        category,
        budget,
        preference
    )

    print("\n========== TOP RECOMMENDATIONS ==========\n")

    if recommendations.empty:
        print("No matching products found.")
        return

    for index, (_, product) in enumerate(
        recommendations.iterrows(), 1
    ):
        print(f"{index}. {product['name']}")
        print(f"   Price   : ₹{product['price']}")
        print(f"   Rating  : ⭐ {product['rating']}")
        print(f"   Features: {product['features']}")
        print()

    print("========== AI RECOMMENDATION ==========\n")

    explanation = generate_ai_response(
        user_query,
        recommendations
    )

    print(explanation)


# -----------------------------
# 5. Run Agent
# -----------------------------

if __name__ == "__main__":
    recommendation_agent()