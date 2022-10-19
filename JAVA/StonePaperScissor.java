import java.util.*;
import java.util.Random;
public class StonePaperScissor {
	public String input()
	{
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter your choice 's' for stone 'p' for paper 'c' for scissors:");
		String choice = sc.nextLine();
		return choice;
	}
	String number_to_string(int h) {
		if (h == 0)
			return "paper";
		else if (h == 1)
			return "scissors";
		else
			return "stone";
	}
	public String choice_to_word(String ch) {
		if (ch.charAt(0) == 'p')
			return "paper";
		else if (ch.charAt(0) == 'c')
			return "scissors";
		else if (ch.charAt(0) == 's')
			return "stone";
		else
		 return "";
	}
	int string_to_number(String choose) {
		if (choose == "paper")
			return 0;
		else if (choose == "scissors")
			return 1;
		else if(choose=="stone")
			return 2;
		else 
		return 9;
	}

	void choice_result(int num, int comp) {
		if (((num - comp) % 3) == 1)
			System.out.println("You won😎😎");
		else if (comp == num)
			System.out.println("Tie");
		else
			System.out.println("Computer won🤓🤓");
	}

	public static void main(String args[]) {
		//int i = 1;
		while (true) {
			Random num = new Random();
			int co = num.nextInt(3);
			gaming ob = new gaming();
			String computer = ob.number_to_string(co);
			String choi = ob.input();
			String cg = ob.choice_to_word(choi);
			System.out.println("Your choice = " + cg);
			System.out.println("Computer choice = " + computer);
			int hum = ob.string_to_number(cg);
			int com = ob.string_to_number(computer);
			ob.choice_result(hum, com);
			System.out.println();
		}
	}
}
