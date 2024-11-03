import keyboard


def main():
    numbers = []
    current_number = ''

    print("Enter 5 numbers with spaces between:")

    while len(numbers) < 5:
        try:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                key = event.name
                if key == 'space':
                    if current_number:
                        numbers.append(float(current_number))
                        current_number = ''
                        if len(numbers) == 5:
                            break
                elif key.isdigit() or key == '.':
                    current_number += key
                elif key == 'enter':
                    break
        except KeyboardInterrupt:
            break

    if current_number:
        numbers.append(float(current_number))

    if numbers:
        print()
        print(f" numbers: {' '.join(map(str, numbers))}")
        average = sum(numbers) / len(numbers)
        print(f" average numbers: {average}")
    else:
        print()
        print("No number entered")
main()

