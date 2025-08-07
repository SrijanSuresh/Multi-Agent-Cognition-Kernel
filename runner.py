from core.core_kernel import CoreKernel

def main():
    kernel = CoreKernel()
    while True:
        user_input = input("Enter a command: ")
        if user_input.lower() == "exit":
            break
        response = kernel.process_input(user_input)
        print(f"Response: {response}")
        kernel.print_log()

if __name__ == "__main__":
    main()
