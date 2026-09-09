public class conditionalstatement {
    public static void main(String[] args) {
        // if else statement
        int age=20;
        if(age>18){
            System.out.println("You are eligible to vote");
        }
        else{
            System.out.println("You are not eligible to vote"); 
        }

        // if else if statement
        int marks=85;   
        if(marks>=90){
            System.out.println("Grade A");
        }
        else if(marks>=80){
            System.out.println("Grade B");
        }
        else if(marks>=70){
            System.out.println("Grade C");
        }
        else{
            System.out.println("Grade D");
        }
        // nested if statement
        int number=10;
        if(number>0){
            if(number%2==0){
                System.out.println("The number is positive and even");
            }
            else{
                System.out.println("The number is positive and odd");
            }
        }
        else{
            System.out.println("The number is negative");
        }
        // // switch statement
        // int day=3;
        // switch(day){
        //     case 1:
        //     System.out.println("Monday");
        //     break;
        //     case 2:
        //     System.out.println("Tuesday");
        //     break;
        //     case 3:
        //     System.out.println("Wednesday");
        //     break;
        //     case 4:
        //     System.out.println("Thursday");
        //     break;

        //     case 5:
        //     System.out.println("Friday");
        //     break;
        //     case 6:
        //     System.out.println("Saturday");
        //     break;
        //     case 7:
        //     System.out.println("Sunday");
        //     break;
        //     default:
        //     System.out.println("Invalid day");

        // ternary operator
        int num1=10;
        int num2=20;
        int max=(num1>num2)?num1:num2;
        System.out.println("Maximum number is: " + max);

        // break statement
        for(int i=1;i<=10;i++){
            if(i==5){
                break;
            }
            System.out.println(i);  

        }
        // continue statement
        for(int j=1;j<=10;j++){
            if(j==5){
                continue;

            }
            System.out.println(j);
            
        }

        // for loop
        for(int k=0;k<5;k++){
            System.out.println("Value of k: " + k);
        }

        // while loop
        int l=0;
        while(l<5){
            System.out.println("Value of l: " + l);
            l++;
        }
        //do while loop
        int m=0;
        do{
            System.out.println("Value of m: " + m);
            m++;}
        while(m<5); 
        

}
    }
