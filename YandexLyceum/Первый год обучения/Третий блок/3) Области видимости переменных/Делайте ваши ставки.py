busy = {}


def do_bet(horse_number, bet):
    if horse_number not in busy and bet != 0 and 0 < horse_number < 11:
        busy[horse_number] = bet
        print(f"Ваша ставка в размере {bet} на лошадь {horse_number} принята")
    else:
        print("Что-то пошло не так, попробуйте еще раз")
