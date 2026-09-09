// public class arrayreversemethod2 {
//     public static void main(String []args){
//         int arr[]={1,2,3,4,5};
//         int n=arr.length;
//         int start=0;
//         int end=n-1;
//         while(start<end){
//             int temp=arr[start];
//             arr[start]=arr[end];
//             arr[end]=temp;
//             start++;
//             end--;


//         }
//         for (int i=0;i<n;i++){
//             System.out.print(arr[i]+" ");
//         }
//     }
    
// }
//using scanner
import java.util.Scanner;
public class arrayreversesmethod2{
    public static void main(String []args){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the size of the array:");
        int n=sc.nextInt();
        System.out.println("Enter the elements of the array:");
        int arr[]=new int[n];
        for(int i=0;i<n;i++){
            arr[i]=sc.nextInt();
        }
        int start=0;
        int end=n-1;    
        while(start<end){
            int temp=arr[start];
            arr[start]=arr[end];
            arr[end]=temp;
            start++;
            end--;
        }
        System.out.println("Reversed array:");
        for (int i=0;i<n;i++){
            System.out.print(arr[i]+" ");
        }

        
        
}}
