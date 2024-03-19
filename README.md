# Open Space Detectives: Unveiling Open Work Areas with Computer Vision
A proof-of-concept pipeline to detect empty seats in common work areas.

## Running Locally
Clone or download this repo
```
git@github.com:MDass/open-space-detectives.git
```

Add a .env file in this directory the following line:
```
OPENAI_API_KEY = "[YOUR OPEN AI KEY]"
```

To train a custom YOLOv8 model, see:
```
finetune_yolo.py
```

To run inference on the custom models we generated, see:
```
run_inference.ipynb
```

To see our Person-Chair Collision Algorithm that detects whether a a person's bounding box collides with a chair's bounding box given out-of-the-box YOLOv8 'person' and 'chair' labels, see:
```
person_chair_collision.py
```

## Credits
Open Space Detectives was created by Michelle Liu and Megan Dass, which was the result of a class project at Stanford University.


## License
The software is available under the [MIT License](https://github.com/poloclub/skeletricks/blob/main/LICENSE).

## Contact
If you have any questions, feel free to [open an issue](https://github.com/MDass/llm_case_law/issues/new) or contact [Megan Dass](mailto:mdass9@stanford.edu) or [Shruti Verma](mailto:shrutive@stanford.edu).