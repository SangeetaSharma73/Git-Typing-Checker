import time
import random
import keyboard
dic={}
def login():
    name = input("Enter your name: ")
    if name in dic:
        raise NameError
    dic[name]=0
    return name

def calculate_wpm(words_typed, time_taken):
    words_per_minute = (words_typed / 5) / (time_taken / 60)
    return round(words_per_minute, 2)

def start_typing():
    text=["In the heart of a tranquil town, an ancient library cradled forgotten tales. Emma, a curious girl, unearthed a dusty book one day. As its pages unfurled, she danced through enchanted realms. Emma's daily returns breathed life into the neglected haven, transforming it into a sanctuary of imagination. Word of her discoveries spread, and soon, the library echoed with laughter. Inspired by Emma's tales, the townsfolk rekindled their love for reading. The once-silent library emerged as a testament to the profound impact a single, dusty book, and an inquisitive spirit, could have on an entire community, unveiling the magic within forgotten stories.",
      "In a quiet town, nestled between hills and meadows, stood an ancient library. One day, a curious girl named Emma discovered a dusty, forgotten book tucked away in a corner. As she opened its pages, she was transported to magical realms and enchanted adventures. Emma returned every day, unlocking new worlds within the library's forgotten books. Soon, she shared her discoveries, and the once-deserted library blossomed into a haven of imagination. The townsfolk, inspired by Emma's tales, rediscovered the joy of reading. The library, once silent, echoed with laughter and stories—a testament to the transformative power of a single, magical discovery.",
      "In a quiet village, a reclusive artist named Lily lived alone. One day, a curious child named Mia knocked on Lily's door, drawn by the vibrant paintings glimpsed through the window. Lily, initially hesitant, welcomed Mia into her world. As they spent the afternoon together, Lily's heart warmed, and her home echoed with laughter. Mia's infectious joy rekindled Lily's own forgotten happiness. Grateful, Lily gifted Mia a small painting of a radiant sun. Little did she know, Mia cherished that painting, and the once-solitary artist found the warmth of friendship lighting up her life, one smile at a time.",
      "In the quiet town of Eldridge, a mysterious old bookstore appeared overnight, its windows filled with dusty volumes and secrets. Intrigued, young Emily wandered in, drawn to a weathered book titled Chronicles of Whispers. As she flipped its pages, tales of enchanted realms and forgotten magic unfolded. The bookstore's eccentric owner, Mr. Hawthorne, appeared, revealing himself as a guardian of forgotten stories. Emily, now entrusted with the ancient book, discovered her role in preserving fading tales. Eldridge transformed into a haven for imagination, as stories once lost found new life. The town whispered gratitude, and Emily became its living legend.",
      "Amelia's antique shop held more than relics—it harbored untold histories. One day, a peculiar pocket watch caught her eye. Its hands ticked backward, defying time. Intrigued, Amelia wound it, unwittingly unlocking a portal to 19th-century London. Startled, she encountered a dapper inventor, lost in time. As they navigated the city's cobblestone streets, a bond blossomed. The pocket watch became a conduit, bridging eras. With each winding, Amelia and her newfound friend traded tales of their worlds. Eventually, the watch's magic faded, leaving them in their respective times. Yet, the connection endured, proving that some friendships transcend the ticking hands of time.",
      "The sun dipped below the horizon, casting long shadows on the deserted beach. Sarah, lost in thought, stumbled upon a mysterious bottle half-buried in the sand. Intrigued, she uncorked it, releasing a swirl of blue mist. To her surprise, a genie materialized, offering three wishes. Bewildered but excited, Sarah wished for happiness, love, and adventure. The genie smiled, granting her wishes in a heartbeat. As Sarah's life transformed, she realized the true magic was within herself.",
      "In the attic, Emma discovered a dusty, forgotten journal. Its pages chronicled the extraordinary life of her great-grandmother, a time-traveling adventurer. With each turn, Emma found herself transported to different eras, experiencing history firsthand. The journal's last entry revealed a crucial choice that shaped her family's destiny. Emma, now armed with newfound knowledge, faced the same decision. History repeated itself as she bravely chose love over fear, altering the course of time and securing a brighter future for generations to come.",
      "The old bookstore harbored more than dusty shelves and yellowed pages. Grace stumbled upon an ancient tome containing forgotten spells. Intrigued, she whispered an incantation, unknowingly unlocking a portal to a magical realm. As the portal enveloped her, Grace found herself in a fantastical world of talking creatures and floating islands. Tasked with a quest to save the realm, she discovered courage within. With a heart full of determination, Grace faced challenges, befriended mythical beings, and, in the end, closed the portal, leaving behind a world forever changed.",
      "On the park bench, two strangers exchanged fleeting glances. A gust of wind sent a scrap of paper spiraling between them. It held a single word: Courage. Intrigued, they embarked on a spontaneous adventure, confronting fears and embracing the unknown. Through laughter and vulnerability, they discovered a connection that transcended time. As the sun set, casting a warm glow on their shared memories, the strangers realized that sometimes, courage is found in the simplest of moments and the most unexpected places.",
      "In a quaint village, a quirky inventor unveiled his latest creation: a device that could capture and relive dreams. Curious villagers lined up, eager to experience forgotten fantasies and nightmares. As dreams unfolded on a magical screen, emotions echoed through the crowd. The once-isolated village transformed into a community bonded by shared dreams. The inventor, beaming with pride, realized that the true magic lay not in the device but in the power of dreams to unite hearts and create a tapestry of collective imagination."
    ]
    random_text = random.choice(text)
    print(random_text)

    input("Press Enter when you are ready to start typing.")

    start_time = time.time()
    user_input = input("Type here: ")
    end_time = time.time()

    words_typed = len(user_input.split())
    time_taken = end_time - start_time

    wpm = calculate_wpm(words_typed, time_taken)

    errors = sum(1 for i, j in zip(random_text.split(), user_input.split()) if i != j)

    print("\nTyping Test Result:")
    print(f"Words per minute: {wpm}")
    print(f"Errors: {errors}")

    return wpm, errors