
from dataclasses import dataclass, field

@dataclass

   
class smartwatch:
    data: dict = field(default_factory=dict)
    
    def smartwatch_datafile(self):
        self.data={
        # greetings & general support
        "hi": "hello! welcome to techgadget support. how can i assist you today?",
        "hello how are you": "hello! welcome to techgadget support. how can i assist you today?",
        "hey": "hey there! welcome to techgadget support. how can i help you today?",
        "good morning": "good morning! welcome to techgadget support. how can i assist you today?",
        "good afternoon": "good afternoon! welcome to techgadget support. how can i assist you today?",
        "good evening": "good evening! welcome to techgadget support. how can i assist you today?",
        "help": "sure! how can i assist you today?",
        "assistance": "i'm here to help! what do you need assistance with?",
        "support": "welcome to techgadget support! how can i support you today?",
        "bye": "thank you for visiting techgadget. if you have more questions, feel free to ask. goodbye!",
        "goodbye": "thank you for visiting techgadget. if you have more questions, feel free to ask. goodbye!",
        "contact support": "you can contact our support team via email at support@techgadget.com or call us at  +91 00000 00000.",
        "chat with a human": "if you prefer to chat with a human, our support team is available 24/7. click the 'chat with a human' button on our website.",

        # product & purchase information
        "do you have smart watches": "yes, we have a variety of smartwatches. you can check them out on our products page.",
        "latest models": "check our latest models section on the website to see the newest arrivals.",
        "product specifications": "detailed specifications of each product can be found on the individual product pages.",
        "features of smartwatches": "our smartwatches offer features like heart rate monitoring, gps, sleep tracking, and customizable watch faces.",
        "ram & storage": "our smartwatches come with varying ram capacities, typically ranging from 512mb to 2gb, and internal storage options from 4gb to 32gb.",
        "processor": "smartwatches are powered by efficient processors like the qualcomm snapdragon wear series or apple's s-series chips.",
        "display type": "smartwatches feature high-resolution displays, such as amoled, oled, or retina displays for crisp and vibrant visuals.",
        "connectivity": "smartwatches support various connectivity options like bluetooth, wi-fi, nfc, and lte, ensuring seamless communication and functionality.",

        # shipping & returns
        "shipping time": "shipping usually takes 3-5 business days.",
        "shipping methods": "we offer standard, expedited, and overnight shipping.",
        "international shipping": "we offer international shipping to most countries. check our shipping page for details and rates.",
        "return policy": "you can return products within 30 days of receipt for a full refund.",
        "how to return": "to return a product, please visit our returns page for a step-by-step guide.",
        "exchange policy": "you can exchange products within 30 days of receipt. visit our exchange page for more details.",

        # troubleshooting & support
        "won’t turn on": "make sure your gadget is charged. if it still won’t turn on, you can visit our troubleshooting page.",
        "reset device": "to reset your device, hold down the power button for 10 seconds. if that doesn't work, please check the manual for a factory reset.",
        "troubleshooting": "for troubleshooting issues, please visit our troubleshooting page or contact our support team.",
        "user manual": "you can download the user manual for your device from our support page.",
        "firmware updates": "check for firmware updates on our support page to ensure your device is up-to-date.",

        # warranty & policies
        "warranty info": "all our products come with a 1-year warranty. for more information, check our warranty page.",
        "store hours": "our store is open from 9 am to 9 pm, monday to saturday.",
        "tracking order": "you can track your order using the tracking number sent to your email. visit our tracking page for more details.",

        # smartwatch features & setup
        "compatible apps": "our smartwatches are compatible with both android and ios devices. you can download our app from the google play store or apple app store.",
        "change watch band": "to change the watch band, refer to the instructions in the user manual or visit our support page for a video tutorial.",
        "set up notifications": "to set up notifications, open the app on your phone and navigate to the notifications settings.",
        "pair with phone": "to pair your smartwatch with your phone, ensure bluetooth is enabled and follow the pairing instructions in the user manual.",
        "sync data": "to sync data between your smartwatch and phone, open the app and select 'sync' from the menu.",
        "update software": "to update the software on your smartwatch, ensure it is connected to wi-fi and follow the update instructions in the app.",
        "adjust brightness": "to adjust the brightness on your smartwatch, go to the settings menu and select 'display' to make the necessary adjustments.",
        "change language": "to change the language on your smartwatch, go to the settings menu and select 'language'. choose your preferred language from the list.",
        "enable gps": "to enable gps on your smartwatch, go to the settings menu and select 'location' to turn on gps functionality.",

        # payments & discounts
        "payment options": "we accept all major credit cards, paypal, and bank transfers.",
        "gift cards": "we offer gift cards that you can purchase on our website. they make great presents for friends and family!",
        "discounts": "check our promotions page for the latest discounts and special offers.",
        "special offers": "our special offers section has all the current promotions and discounts.",

        # combined "battery" related responses
        "battery": "the battery life of our smartwatches ranges from 24 to 48 hours, depending on usage. "
                "for battery replacement services, visit our support page or contact our team. "
                "power through your day with the robust 400mah battery, enjoying all smartwatch features without frequent recharging.",

        # smartwatch functionalities
        "health & fitness tracking specification configuration": "our smartwatches offer features like heart rate monitoring, spo2 monitoring, sleep tracking, step counter, activity tracking, ecg, stress & hrv monitoring, and menstrual cycle tracking.",
        "fitness & sports features": "track and optimize your performance across various exercise routines with multiple sports modes, vo2 max measurement, ai coaching & guided workouts.",
        "smart features & customization": "enjoy smart features like music & media control, custom watch faces, smart home integration, and weather updates.",
        "safety & emergency features": "stay safe with features like fall detection & emergency sos, car crash detection, and geofencing & location sharing.",
        "4g volte calling": "stay connected even without your phone! enjoy seamless voice calls over 4g nano-sim networks right from your wrist.",
        "gps functionality": "track your course effortlessly with the built-in gps feature for precise location tracking during outdoor activities.",
        "ip67 water resistant": "embrace any adventure confidently with ip67 water resistance, protecting your smartwatch from sweat and rain.",

        # miscellaneous
        "what are the best smartwatches available right now?": "the best smartwatches depend on your needs. popular options include apple watch series, samsung galaxy watch, garmin, and fitbit.",
        "how does a smartwatch work?": "a smartwatch works by connecting to your smartphone via bluetooth or lte and provides notifications, health tracking, and smart features.",
        "are smartwatches worth buying?": "if you want fitness tracking, notifications, and convenience on your wrist, a smartwatch is a great investment.",
        "is this smartwatch compatible with my smartphone (android/iphone)?": "most smartwatches support both android and ios, but apple watches only work with iphones.",
        "does it support bluetooth, wi-fi, or lte?": "most smartwatches have bluetooth and wi-fi; premium models offer lte for independent calling and data usage.",

        "general": "smartwatch, wearable technology, digital watch, fitness tracker, health watch, touchscreen watch, smart band",
        "features_specifications": "heart rate monitor, gps tracking, sleep tracking, step counter, activity tracker, spo2 monitoring, ecg sensor, stress monitoring, blood pressure monitor, menstrual cycle tracking, ai coaching, guided workouts, waterproof smartwatch, ip67/ip68 rating, customizable watch faces, always-on display, amoled/oled/retina display, voice assistant",
        "connectivity_communication": "bluetooth smartwatch, wi-fi enabled watch, lte smartwatch, 4g volte calling, nfc payments, mobile notifications, sms & call alerts, smartwatch with esim",
        "battery_performance": "long battery life, fast charging, power-saving mode, wireless charging",
        "smart_features_integration": "music control, smart home integration, voice control, google assistant, siri compatible, amazon alexa support, app synchronization",
        "brands_compatibility": "apple watch, samsung galaxy watch, garmin smartwatch, fitbit watch, huawei smartwatch, oneplus watch, android smartwatch, ios compatible watch",
        "price": "budget smartwatch, affordable smartwatch, mid-range smartwatch, premium smartwatch, best smartwatch under 5000, best smartwatch under 10000, best smartwatch under 20000, luxury smartwatch"

        }
        return self.data

