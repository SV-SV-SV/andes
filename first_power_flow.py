import andes


def main():
    # Najdi soubor s modelem sítě IEEE 14 a načti jej.
    case_file = andes.get_case("ieee14/ieee14_fault.xlsx")
    system = andes.load(case_file)

    # Vypočti ustálený stav sítě před poruchou.
    system.PFlow.run()

    print("Počet uzlů:", system.Bus.n)
    print("Výpočet konvergoval:", system.PFlow.converged)


if __name__ == "__main__":
    main()