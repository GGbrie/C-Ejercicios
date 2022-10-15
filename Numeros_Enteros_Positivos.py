using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
 
namespace NumerosEnterosPositivos
{
    class Program
    {
        static void Main(string[] args)
        {
            int num;
            string linea;
            Console.Write("Dame tres numeros positivos:");
            linea = Console.ReadLine();
            num=int.Parse(linea);
            if (num<10) 
            {
	            Console.Write("Solo tiene un dígito");
            }
            else 
            {
                if (num<100) 
                {
                    Console.Write("Solo tiene dos dígitos");
                }
                else 
                {
                    if (num<1000) 
                    {
                        Console.Write("Tiene tres dígitos");
                    }
                    else 
                    {
                        Console.Write("Error: Intentalo de Nuevo");
                    }
                }
            }
            Console.ReadKey();
        }
    }
}