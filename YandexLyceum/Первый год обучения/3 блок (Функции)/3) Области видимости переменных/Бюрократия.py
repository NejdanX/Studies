employee_number = -1
employee_list = []


def setup_profile(name, vacation_dates):
    employee_list.append((name, vacation_dates))
    global employee_number
    employee_number += 1


def print_application_for_leave():
    print(f"Заявление на отпуск в период {employee_list[employee_number][1]}. {employee_list[employee_number][0]}")


def print_holiday_money_claim(amount):
    print(f"Прошу выплатить {amount} отпускных денег. {employee_list[employee_number][0]}")


def print_attorney_letter(to_whom):
    print(f"На время отпуска в период {employee_list[employee_number][1]} моим заместителем назначается "
          f"{to_whom}. {employee_list[employee_number][0]}")
