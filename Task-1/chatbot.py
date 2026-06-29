from datetime import datetime

print("=" * 55)
print("        DailyCompanion - Wellness Chatbot")
print("=" * 55)

print("\nI can help you with the following:\n")

print("✅ Personalized Greetings")
print("✅ Daily Wellness Tips")
print("✅ Healthy Eating Suggestions")
print("✅ Water Intake Advice")
print("✅ Exercise Recommendations")
print("✅ Motivational Quotes")
print("✅ Current Date & Time")
print("✅ Fun Facts & Jokes")
print("✅ Exit Message")

print("\nExamples:")
print("• hi")
print("• health tip")
print("• diet")
print("• water")
print("• exercise")
print("• motivate me")
print("• joke")
print("• fun fact")
print("• time")
print("• date")
print("• help")
print("• bye")

print("\nType 'bye' anytime to exit.\n")

while True:
    user = input("You: ").lower().strip()

    if user in ["hi", "hello", "hey"]:
        print("Bot: Hello! Hope you're having a wonderful day.")

    else:
        if "health" in user or "wellness" in user:
            print("Bot: Eat nutritious food, stay hydrated, exercise regularly, and get enough sleep.")

        else:
            if "diet" in user or "food" in user:
                print("Bot: Include fruits, vegetables, whole grains, and protein in your daily meals.")

            else:
                if "water" in user:
                    print("Bot: Try to drink at least 8 glasses of water every day.")

                else:
                    if "exercise" in user or "workout" in user:
                        print("Bot: A 30-minute walk or light exercise every day helps keep you healthy.")

                    else:
                        if "motivate" in user or "motivation" in user:
                            print("Bot: Believe in yourself. Small daily efforts lead to big success!")

                        else:
                            if "joke" in user:
                                print("Bot: Why did the computer go to the doctor? Because it caught a virus!")

                            else:
                                if "fact" in user:
                                    print("Bot: Fun Fact: Laughing for 10 minutes can help reduce stress.")

                                else:
                                    if "time" in user:
                                        print("Bot: Current Time:", datetime.now().strftime("%I:%M:%S %p"))

                                    else:
                                        if "date" in user:
                                            print("Bot: Today's Date:", datetime.now().strftime("%d-%m-%Y"))

                                        else:
                                            if "help" in user:
                                                print("\nBot: I can help you with:")
                                                print("- Greetings")
                                                print("- Health Tips")
                                                print("- Healthy Diet")
                                                print("- Water Intake")
                                                print("- Exercise")
                                                print("- Motivation")
                                                print("- Jokes")
                                                print("- Fun Facts")
                                                print("- Current Time")
                                                print("- Current Date")
                                                print("- Type 'bye' to exit.")

                                            else:
                                                if user == "bye":
                                                    print("Bot: Goodbye! Stay healthy and have a wonderful day.")
                                                    break

                                                else:
                                                    print("Bot: Sorry, I don't understand that. Type 'help' to see my features.")
