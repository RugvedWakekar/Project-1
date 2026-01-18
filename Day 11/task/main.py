import random
def blackjack():
    def card_drawing():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        def start():
            user = []
            for user_key in range(1,3):
                user += [random.choice(cards)]

            computer = []
            for comp_key in range(1,3):
                computer += [random.choice(cards)]
            again_input = input("Do you want to play a game of Blackjack? Type 'y' or 'n' \n")
            if again_input == 'y':
                import art
                print(art.logo)
                current_score = sum(user)
                print(f"Your cards: {user}, current score:{current_score}\nComputer's first card: {computer[0]}")

                should_continue= True
                while should_continue:
                    while sum(user) < 16:
                        again = input("Type 'y' to get another card, type 'n' to pass: ")
                        if again == 'y':
                            user += [random.choice(cards)]
                            print(f"Your cards: {user}, current score: {sum(user)}\nComputer's first card: {computer[0]}")

                            if sum(user) > 21:
                                print(f"Your final hand: {user}, final score: {sum(user)}\n"
                                          f"Computer's final hand: {computer}, final score: {sum(computer)}\n"
                                          f"You went over. You lose 😭")
                                should_continue = False
                                start()
                            elif sum(user) > 16:
                                for eleven in user:
                                    if eleven == 11 and sum(user) >=0 and sum(user) <= 16:
                                        user.remove(11)
                                        user.append(1)
                                        print(f"your cards: {user}, current score: {sum(user)}\n"
                                              f"Computer's first card: {computer[0]}")
                            elif sum(user) > sum(computer):
                                print(f"Your final hand: {user}, final score: {sum(user)}\n"
                                      f"Computer's final hand: {computer}, final score: {sum(computer)}\n"
                                      f"You went over. You lose 😭")
                            elif sum(user) < sum(computer):
                                print(f"Your final hand: {user}, final score: {sum(user)}\n"
                                      f"Computer's final hand: {computer}, final score: {sum(computer)}")
                                print("You Win 😃")
                            elif sum(user) == sum(computer):
                                print(f"Your final hand: {user}, final score: {sum(user)}\n"
                                      f"Computer's final hand: {computer}, final score: {sum(computer)}")
                                print("It's a draw 🤯")
                            elif sum(user) == 21:
                                print(f"Your final hand: {user}, final score: {sum(user)}\n"
                                      f"Computer's final hand: {computer}, final score: {sum(computer)}")
                                print("You Win 😃")
                            elif sum(computer) == 21:
                                print(f"Your final hand: {user}, final score: {sum(user)}\n"
                                      f"Computer's final hand: {computer}, final score: {sum(computer)}\n"
                                      f"You went over. You lose 😭")
                            else:
                                print("Invalid, restart program")

                        elif again == 'n':

                            if sum(user) > 21:
                                print(f"Your final hand: {user}, final score: {sum(user)}\n"
                                          f"Computer's final hand: {computer}, final score: {sum(computer)}\n"
                                          f"You went over. You lose 😭")
                                should_continue = False
                                start()
                            elif sum(user) > 16:
                                for eleven in user:
                                    if eleven == 11 and sum(user) >=0 and sum(user) <= 16:
                                        user.remove(11)
                                        user.append(1)
                                        print(f"your cards: {user}, current score: {sum(user)}\n"
                                              f"Computer's first card: {computer[0]}")
                            elif sum(user) > sum(computer):
                                print(f"Your final hand: {user}, final score: {sum(user)}\n"
                                      f"Computer's final hand: {computer}, final score: {sum(computer)}\n"
                                      f"You went over. You lose 😭")
                            elif sum(user) < sum(computer):
                                print(f"Your final hand: {user}, final score: {sum(user)}\n"
                                      f"Computer's final hand: {computer}, final score: {sum(computer)}")
                                print("You Win 😃")
                            elif sum(user) == sum(computer):
                                print(f"Your final hand: {user}, final score: {sum(user)}\n"
                                      f"Computer's final hand: {computer}, final score: {sum(computer)}")
                                print("It's a draw 🤯")
                            elif sum(user) == 21:
                                print(f"Your final hand: {user}, final score: {sum(user)}\n"
                                      f"Computer's final hand: {computer}, final score: {sum(computer)}")
                                print("You Win 😃")
                            elif sum(computer) == 21:
                                print(f"Your final hand: {user}, final score: {sum(user)}\n"
                                      f"Computer's final hand: {computer}, final score: {sum(computer)}\n"
                                      f"You went over. You lose 😭")
                            else:
                                print("Invalid, restart program")

                        else:
                            print('Invalid input')

                print(cards[0])
            elif again_input == 'n':
                exit()

        start()
    card_drawing()
blackjack()
