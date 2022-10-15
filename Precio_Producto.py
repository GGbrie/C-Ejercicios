using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace PreciodeunProducto
{
    class Program
    {
        static void Main(string[] args)
        {
            int cantidad;
            float  PrecioArticulo, ValorVenta;
            string linea;

            Console.Write("Precio del artProducto:");
            linea = Console.ReadLine();
            PrecioArticulo = float.Parse(linea);
            Console.Write("Cantidad de articulos a comprar por el cliente:");
            linea = Console.ReadLine();
            cantidad = int.Parse(linea);

            ValorVenta = PrecioArticulo * cantidad;
            Console.Write("El Total serian:");
            Console.WriteLine(ValorVenta);
            Console.ReadKey();

        }
    }
}
