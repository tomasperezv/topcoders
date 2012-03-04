package MatchMaker;

class MatchMaker {

	public final static int POS_USER = 0;
	public final static int POS_GENDER = 1;
	public final static int POS_GENDER_REQUESTED = 2;
	public final static int MAX_MEMBERS = 50;

	public String[] currentUserSFData;
	public int currentUserPos;
	public String currentUserGender;

	public void MatchMaker() {
		// Do nothing
	}

	public String[] getBestMatches(String[] param0, String param1, int param2) {

		int i, numUsers, currentPos, currentName, resultPos;
		String currentGender;

		String[] currentSFData;
		String[] currentUserSFData;

		numUsers = param0.length;

		// Input checks
		if (numUsers <1 || numUsers > this.MAX_MEMBERS) {
			return null;
		}

		// The result has as maximum numUsers - 1 positions
		String[] result = new String[numUsers-1];

		// Search the current user in the array of member to generate currentUserSFData
		for (i = 0; i <  numUsers ; i++ ) {
			currentSFData = param0[i].split(" ");

			if (currentSFData.length < 7 || currentSFData.length > 44) {
				// Invalid input
				System.out.println("invalid input for SF data");
				return null;
			}

			// Check the name
			if (currentSFData[this.POS_USER].length() < 1 || currentSFData[this.POS_USER].length() > 20 || !currentSFData[this.POS_USER].matches("[A-Z]+")){
				System.out.println("invalid length or string in a name");
				return null;
			}

			// Check the gender
			if (!currentSFData[this.POS_GENDER].matches("[MF]+")) {
				System.out.println("invalid gender in data");
				return null;
			}

			// Check the gender requested
			if (!currentSFData[this.POS_GENDER_REQUESTED].matches("[MF]+")) {
				System.out.println("invalid gender requested in data");
				return null;
			}

			// We discard the current user to generate the matrix of data.
			if (param1.toUpperCase().equals(currentSFData[this.POS_USER].toUpperCase())) {
				this.currentUserPos = i;
				this.currentUserSFData = currentSFData;
				this.currentUserGender = currentSFData[this.POS_GENDER];
				break;
			}
		}
	
		// First generate the array with sf's
		Integer[] matrixSF = new Integer[numUsers-1];
		currentPos = 0;
		resultPos = 0;

		for (i = 0; i <  numUsers ; i++ ) {
			currentSFData = param0[i].split(" ");
			currentGender = currentSFData[this.POS_GENDER];
			// We discard the current user to generate the matrix of data.
			if (i != this.currentUserPos && !this.currentUserGender.equals(currentGender)) {
				if (this.countMatches(currentSFData) >= param2) {
					result[resultPos] = currentSFData[this.POS_USER];
					resultPos++;
				}
			}
		}

		return result;
	}


	protected int countMatches(String[] sfData) {
		int i, numQuestions;
		String question;
		int numMatches = 0;
		numQuestions = sfData.length - 1;

		if (numQuestions > 10 || numQuestions < 1) {
			return -1;
		}

		for ( i = 0 ; i < numQuestions ; i++ ) {
			if (i != this.POS_USER && i!= this.POS_GENDER && i!= this.POS_GENDER_REQUESTED) {
				question = this.currentUserSFData[i];
				
				// Check the validity of the question
				if (!question.matches("[A-D]+")) {
					System.out.println("invalid question");
					return -1;
				}

				if (sfData[i].equals(question))
				{
					numMatches++;
				}
			}
		}
		return numMatches;
	}
}

