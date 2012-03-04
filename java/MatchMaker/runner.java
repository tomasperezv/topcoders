package MatchMaker;

public class runner {
	public static void main(String[] args) {

		// Prepare the input params
		String[] members = new String[8];
		members[0] = new String("BETTY F M A A C C");
		members[1] = new String("TOM M F A D C A");
		members[2] = new String("SUE F M D D D D");
		members[3] = new String("ELLEN F M A A C A");
		members[4] = new String("JOE M F A A C A");
		members[5] = new String("ED M F A D D A");
		members[6] = new String("SALLY F M C D A B");
		members[7] = new String("MARGE F M A A C C");
		int sf = 1;
		int i;
		String currentUser = new String("JOE");

		MatchMaker matchMaker = new MatchMaker();
		String[] result = matchMaker.getBestMatches(members, currentUser, sf);
		for (i=0;i<result.length;i++) {
			if (result[i] != null) {
				System.out.println("result " + result[i]);
			}
		}

	}
}
