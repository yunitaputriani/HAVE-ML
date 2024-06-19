#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import os
import textwrap
from IPython.display import display, Image, HTML


# In[2]:


# Path ke folder gambar
image_folder_path = 'D:\\BANGKIT\\images'


# In[3]:


# Membuat data dummy rekomendasi olahraga
food_recommendations = [
    {
        "name": "Vagatables",
        "description": "Vegetables of all kinds can assist with weight loss, says Feit. For example, cruciferous vegetables like broccoli, cauliflower, Brussels sprouts and cabbage are high in fiber and vitamins and help reduce digestive issues. Meanwhile, dark green leafy vegetables contain protein and are a good source of vitamins, minerals and fiber. And crunchy vegetables like celery and jicama are great low-calorie options for snacking. A typical serving size of vegetables is about 1 cup (100-150 grams) and can range from 25-75 calories depending on the type of vegetable.",
        "calories": "25-75 Cal",
        "image_filename": "vagatables.jpg"
    },
    {
        "name": "Salmon",
        "description": "Salmon is high in protein and omega-3 fatty acids, says Rima Kleiner, registered dietitian nutritionist and founder of wellness coaching company Smart Mouth Nutrition in Greensboro, North Carolina. Research suggests omega-3 fatty acids may help people with weight classified as overweight or obesity feel fuller[2]. And fish in general may help you feel satisfied and fuller longer than other proteins like eggs and beef, says Kleiner.",
        "calories": "182-206 Cal",
        "image_filename": "salmon.jpg"
    },
    {
        "name": "Shrimp",
        "description": "Shrimp promotes increased feelings of satiety, says Kleiner. Eating shrimp appears to decrease appetite by stimulating the production of cholecystokinin, or CCK, a hormone that signals to your stomach that you’re satisfied. Plus, shrimp and other shellfish contain zinc and selenium, two important minerals for immune health and increased energy. It's quite low in calories, providing only 84 calories in a 3-ounce serving",
        "calories": "84 Cal",
        "image_filename": "shrimp.jpg"
    },
    {
        "name": "Lupini Beans",
        "description": "Lupini beans are high in prebiotic fiber that feeds the beneficial bacteria in your gut, says Landau. “When your gut bacteria is well nourished, the number and type of bacteria present multiplies. A well-populated and diverse microbiome improves gut health, which makes your cells more responsive to insulin, helping to remove fat stored around the waist,” she says. One 1 cup (166g) of lupini beans, cooked and boiled without salt, contains approximately 198 calories",
        "calories": "198 Cal",
        "image_filename": "lupini beans.jpg"
    },
    {
        "name": "Unripe Banana",
        "description": "Unripe banana contain one of the world’s richest sources of prebiotic-resistant starch, says Landau. Prebiotic-resistant starch makes your cells more responsive to insulin, helping to prevent fat storage around your waistline. Combined with protein (say, in a smoothie with a protein powder and/or nut butter), it can keep you satisfied for hours. In addition, it has 121 calories in 120 g.",
        "calories": "121 Cal",
        "image_filename": "unripe banana.jpg"
    }
]

def wrap_text(text, width=80):
    return '\n'.join(textwrap.wrap(text, width))

# Menambahkan path gambar ke setiap data olahraga
for food in food_recommendations:
    food["description"] = wrap_text(food["description"])
    image_path = os.path.join(image_folder_path, food["image_filename"])
    food["image_path"] = os.path.abspath(image_path)


#Menyimpan data dummy dalam file JSON
with open('food_recommendations.json', 'w') as file:
    json.dump(food_recommendations, file, indent=4)

for food in food_recommendations:
    display(HTML(f"<h2>{food['name']}</h2>"))
    display(HTML(f"<p>{food['description']}</p>"))
    display(HTML(f"<p>Calories: {food['calories']}</p>"))
    display(Image(filename=food['image_path']))
    display(HTML("<hr>"))

