// public class arraylearning{
//     public static void main(String[] args) {
//         int arr[]={1,2,3,4,5};
//         System.out.println("Length of array: " + arr.length);
//         System.out.println("Elements of array: ");
//         for(int i=0;i<arr.length;i++){
//             System.out.println(arr[i] + " ");
//         }

//         int arr2[]=new int[5];
//         int ar3[]=new int[6];
//         ar3[0]=1;
//         ar3[1]=2; 
//         ar3[2]=3;
//         ar3[3]=4;
//         ar3[4]=5;
//         System.out.println("Elements of array: ");
//         for(int i=0;i<ar3.length;i++){
//             System.out.println(ar3[i] + " ");
//         }
        

        
//     }
// }
import java.util.Scanner;
public class arraylearning{
    public static void main(String []args){
        Scanner sc=new Scanner (System.in);
        System.out.println("Enter the size of the array:");
        int n=sc.nextInt();
        System.out.println("Enter the elements of the array:");
        int arr[]=new int[n];
        for(int i=0;i<n;i++){
            arr[i]=sc.nextInt();
        }


        System.out.println("Elements of array: ");
        for(int i=0;i<n;i++){
            System.out.print(arr[i] + " ");
        }
    }
}