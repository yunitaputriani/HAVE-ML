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
exercise_recommendations = [
    {
        "name": "Swimming",
        "description": "Swimming is a low-impact workout that burns energy while improving muscle strength, blood flow, and lung and heart capacity. Thirty minutes of casual swimming burns about the same number of calories as 30 minutes of jogging. However, swimming is less stressful on the body. It may be an appropriate exercise if you have joint problems or limited mobility. To increase your caloric burn during swimming, do laps or water aerobics.",
        "calories_burned": "198-294 Cal",
        "image_filename": "swimming.jpg"
    },
    {
        "name": "Hiking-knee Running",
        "description": "High-knee running is a vigorous cardio workout. It raises your heart rate while strengthening your lower body. As a high-intensity exercise, high-knee running is useful for burning calories in a short amount of time. To do this exercise, all you need to do is run in place while lifting your knees as high as possible and quickly pump your arms up and down.",
        "calories_burned": "240-355.5",
        "image_filename": "high-knee running.jpg"
    },
    {
        "name": "Hiking",
        "description": "Hiking is one of the best ways to escape to the outdoors, turn off technology and get in some movement. And since you are not walking on a level path like walking down the street, navigating different terrains or hills challenges more muscles, so you burn more calories.",
        "calories_burned": "176 Cal",
        "image_filename": "hiking.jpg"
    },
    {
        "name": "Biking",
        "description": "There’s nothing like a nice evening bike ride when the weather’s nice, and it’s actually a great workout too. If you are an avid biker, you may go faster than 5.5 mph, but if you tend to bike at a leisurely pace, you can still burn 117 calories per 30 minutes. Note that this is different than if you do interval training or classes on spin bikes.",
        "calories_burned": "210-311 Cal",
        "image_filename": "biking.jpg"
    },
    {
        "name": "Walking",
        "description": "Walking is the simplest way to burn calories at home. It’s also ideal if you’re recovering from an injury. You can do it around your house or in your backyard, so it’s extremely convenient. If you do housework while walking around your home, you’ll burn even more calories per minute.",
        "calories_burned": "3.1-4.6 Cal",
        "image_filename": "walking.jpg"
    }
]

def wrap_text(text, width=80):
    return '\n'.join(textwrap.wrap(text, width))

# Menambahkan path gambar ke setiap data olahraga
for exercise in exercise_recommendations:
    exercise["description"] = wrap_text(exercise["description"])
    image_path = os.path.join(image_folder_path, exercise["image_filename"])
    exercise["image_path"] = os.path.abspath(image_path)


# Menyimpan data dummy dalam file JSON
with open('exercise_recommendations.json', 'w') as file:
    json.dump(exercise_recommendations, file, indent=4)

for exercise in exercise_recommendations:
    display(HTML(f"<h2>{exercise['name']}</h2>"))
    display(HTML(f"<p>{exercise['description']}</p>"))
    display(HTML(f"<p>Calories Burned: {exercise['calories_burned']}</p>"))
    display(Image(filename=exercise['image_path']))
    display(HTML("<hr>"))

