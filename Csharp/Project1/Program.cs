using System;
namespace Project1
{
    class Program
    {
        static void Main(string[] args) // this is the entry method
        {
            Console.Clear();

            Console.Write("Input a number between 1 and 5: ");
            int num = Convert.ToInt32(Console.ReadLine());
            Console.ForegroundColor = ConsoleColor.Green;

            switch (num)
            {
                case 1:
                    Console.WriteLine("One");
                    break;
                case 2:
                    Console.WriteLine("Two");
                    break;
                case 3:
                    Console.WriteLine("Three");
                    break;
                case 4:
                    Console.WriteLine("Four");
                    break;
                case 5:
                    Console.WriteLine("Five");
                    break;
                default:
                    Console.WriteLine("Default");
                    break;
            }

            // Wait before closing
            Console.ReadKey();
        }
    }
}