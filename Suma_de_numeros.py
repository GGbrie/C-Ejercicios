using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Suma_de_numeros
{
    class Program
    {
        static void Main(string[] args)
        {
            int suma,valor;
            string linea;
            suma=0;
            do {
                Console.Write("Ingrese un valor cualquiera:");
                linea = Console.ReadLine();
                valor=int.Parse(linea);
                if (valor!=9999) 
                {
                    suma=suma+valor;
                }
            }while (valor!=9999);
            Console.Write("El valor es:");
            Console.WriteLine(suma);
            if (suma==0) 
            {
                Console.WriteLine("El valor da cero");
            }
            else 
            {
                if (suma>0) 
                {
                    Console.WriteLine("El valor es positivo.");
                } 
                else 
                {
                    Console.WriteLine("El valor es negativo");
                }
            }
            Console.ReadKey();
        }
    }
}
