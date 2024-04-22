from Backend import WG

def main():
    print("Hello Player!")
    wg = WG("SHOAL")

    while wg.Can_Guess:
        x = input("Enter a word: ")

        if len(x) != wg.Chars:
            print(f"Word must have excatly {wg.Chars} letters.")
            continue

        wg.Guess(x)
        result = wg.trial(x)
        print(*result,sep="\n")

    if wg.ans_correct:
        print("Correct")
    else:
        print("Wrong")

if __name__ == "__main__":
    main()

