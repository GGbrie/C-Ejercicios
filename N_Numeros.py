using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace N_Numeros
{
    class Program
    {

static void Main(string[] args)
        {
            int x, n, valor, par, impar;

            x = 1;
            par = 0;
            impar = 0;
            Console.Write("¿Cuántos números desea agregar? :");
            n = Convert.ToInt32(Console.ReadLine());
            while (x<=n)
            {
                Console.Write("Introduzca un valor impar o par");
                valor = Convert.ToInt32(Console.ReadLine());
                if (valor % 2 == 0)
                {
                    par++;
                }
                else if (valor % 2 != 0)
                {
                    impar++;
                }
                x++;
            }
            Console.WriteLine("Números pares: " + par.ToString());
            Console.WriteLine("Números impares: " + impar.ToString());
            Console.ReadKey();
        }
    }
}
