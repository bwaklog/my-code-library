using System;
using System.Collections.Generic;

namespace Project3
{
    class Program
    {
        static void Main(string[] args)
        {
            // Code goes here :)
            Console.WriteLine("Hello");
            // Wait for user input
            Console.ReadKey();
        }

        static void MeetAlien()
        {
            Random numberGen = new Random();

            string name = "X-" + numberGen.Next(10, 9999);
            int age = numberGen.Next(10, 500);

            Console.WriteLine("Hi, I'm " + name + ".");
            Console.WriteLine("I'm " + age + " years old!");
            Console.WriteLine("Oh, and I'm an aline");
        }

        static void printHi()
        {
            Console.WriteLine("Well hello there!");
        }


    }
}