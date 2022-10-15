using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

Lado de un Cuadrado 
{
    Class Program
    {
        static void Main (string[] args)
        {
            int lago, perimetro;
            string linea;

            Conseole.Write("Cual es el lado del Cuadrado? ")
            linea = Console.ReadLine();
            lado = int.Parse(linea);
            Perimetro = lado * 4;
            
            Console.Write("El Perimetro del Cuadrado es: ")
            Console.Write(Perimetro);
            Console.ReadKey();

        }
    }
}