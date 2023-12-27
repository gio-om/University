using System;

namespace ConsoleApp1
{
    class Program
    {
        static int levenshtein_distance(string str1, string str2)
        {
            int len1 = str1.Length;
            int len2 = str2.Length;

            int[,] dp = new int[len1 + 1, len2 + 1];
            
            for (int i = 0; i <= len1; i++)
                dp[i, 0] = i;
            for (int j = 0; j <= len2; j++)
                dp[0, j] = j;

            for (int i = 1; i <= len1; i++)
            {
                for (int j = 1; j <= len2; j++)
                {
                    int cost = (str1[i - 1] == str2[j - 1]) ? 0 : 1;
                    dp[i, j] = Math.Min(
                        dp[i - 1, j] + 1,          
                        Math.Min(
                            dp[i, j - 1] + 1,      
                            dp[i - 1, j - 1] + cost 
                        )
                    );
                }
            }

            return dp[len1, len2];
        }

        static void Main(string[] args)
        {
            Console.Write("Введите первую строку: ");
            string str1 = Console.ReadLine();
            Console.Write("Введите вторуб строку: ");
            string str2 = Console.ReadLine();

            int distance = levenshtein_distance(str1, str2);
            Console.WriteLine($"Расстояние Левенштейна: : {distance}");
        }
    }

}
