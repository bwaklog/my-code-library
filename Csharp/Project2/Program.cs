using System;
using System.Collections.Generic;

namespace Project2
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Clear();

            Console.WriteLine("How many students are in the class");
            int count = Convert.ToInt32(Console.ReadLine());

            string[] students = new string[count];

            Console.Clear();
            for (int i = 0; i < students.Length; i++)
            {
                Console.WriteLine("Enter the names of the students :");
                Console.Write("Index " + i + " : ");
                students[i] = Console.ReadLine();
                Console.Clear();
            }

            Console.Clear();
            Console.WriteLine("List of students in class(in order)");
            Array.Sort(students);
            for (int i = 0; i < students.Length; i++)
            {
                int num = i + 1;
                Console.WriteLine(num + " : " + students[i]);
            }

            // Wait before closing
            // Console.ReadKey();
        }
    }
}