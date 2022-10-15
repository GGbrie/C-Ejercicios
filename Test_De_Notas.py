using System;
 using System.Collections.Generic;
 using System.Linq;using 
 System.Text;
 using System.Threading.Tasks;
 
 namespace TestDeNotas
 
 { 
    class Program 
    { 
        static void Main(string[] args) 
        { 
            int numPreguntas, numContestadas, porcentaje; 
            string linea; Console.Write("Cuantas preguntas eran en el examen?"); 

            linea = Console.ReadLine(); 
            numPreguntas = int.Parse(linea); 
            Console.Write("Cuantas respondiste bien?"); 
            linea = Console.ReadLine(); 
            numContestadas = int.Parse(linea); 
            porcentaje = (numContestadas * 100) / numPreguntas; 

            if (porcentaje >= 90) { Console.Write("¡Su nivel es Máximo, FELICIDAES!"); 
            } 
            else if (porcentaje >= 75) 
            { 
            Console.Write("Su nivel es Medio, DEBE MEJORAR"); 
             } 
            if (porcentaje >= 50 && porcentaje < 75) 
            { 
            Console.Write("Su nivel es regular, ESFUERZATE"); 
            } 
            else if (porcentaje < 50)

            { 
            Console.Write("Fuera de nivel, INTENTALO OTRA VEZ"); 
            } 
            Console.ReadKey(); 

        } 

     }

}