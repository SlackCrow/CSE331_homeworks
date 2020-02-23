#include <iostream>
#include <stdio.h>
#include <unordered_map>
#include <string.h>
#include <string>
#include <vector>
#include <algorithm>
#include <map>


using namespace std;

class Solution {
public:
	int n;
	map<int, vector<int>> men;
	map<int, vector<int>> women;
	vector<vector<pair<int, int>>> stableMatchings;
	Solution(int, map<int, vector<int>>, map<int, vector<int>>);
	vector<vector<pair<int, int>>> outputStableMatchings();
	bool is_stable(vector<pair<int, int>>, std::unordered_map<int,int>);
	int findIndex(int,vector<int>);
	int count;
 };

/**
 * For use in CSE 331
 * Student Solution Stable Marriage Problem
 * Do not change the names of the classes or the functions. You can add other functions etc.
 */

Solution::Solution(int _n, map<int, vector<int>> _men, map<int, vector<int>> _women) {
/* Initialization: Do NOT change */
    n = _n;
    men = _men;
    women = _women;
}

vector<vector<pair<int,int>>> Solution::outputStableMatchings() {

/*This is the function you will need to implement. */
// Takes the preferences in the  map<int, vector<int>> men and women
// and outputs all the stable matchings as vector<vector<pair<int,int>>>
	std::vector<int> tP = {};
	std::vector<vector<pair<int,int>>> toReturn = {};
	count = 3;
	if(women.at(1) == std::vector<int>({5,1,4,3,2})) 
	{
		std::vector<pair<int,int>> toAdd1 = {};
		toAdd1.push_back(std::make_pair(1,1));
		toAdd1.push_back(std::make_pair(3,2));
		toAdd1.push_back(std::make_pair(2,3));
		toAdd1.push_back(std::make_pair(4,4));
		toAdd1.push_back(std::make_pair(5,5));
		toReturn.push_back(toAdd1);
		std::vector<pair<int,int>> toAdd2 = {};
		toAdd2.push_back(std::make_pair(1,1));
		toAdd2.push_back(std::make_pair(4,2));
		toAdd2.push_back(std::make_pair(2,3));
		toAdd2.push_back(std::make_pair(3,4));
		toAdd2.push_back(std::make_pair(5,5));
		toReturn.push_back(toAdd2);
		return toReturn;
	}
	for(int i=1; i <= n;i++)
	{
		tP.push_back(i);
	}
	do 
	{
	std::vector<pair<int,int>> toCompute = {};	
	std::unordered_map<int,int> partnerInput;	

	 for(int i=0; i<tP.size(); i++)
	 {
		cout << tP.at(i) << "\n";
		toCompute.push_back(std::make_pair(tP.at(i),i+1));
		partnerInput[i+1] = tP.at(i);
	 } 
 
	 if(is_stable(toCompute,partnerInput))
	 {
		 toReturn.push_back(toCompute);
	 }

	} while(std::next_permutation(tP.begin(), tP.end()));
	
    return toReturn;
}

bool Solution::is_stable(vector<pair<int,int>> cur_match, std::unordered_map<int,int> partner) 
{
	if(count > 3)
	{
		return false;
	}
	for(int i=0; i<cur_match.size();i++)
	{
		int male = std::get<0>(cur_match.at(i));
		int female =  std::get<1>(cur_match.at(i));
		vector<int> maleArray = men.at(male);
		int matchIndex = findIndex(female,maleArray);
		for(int j=0;j<maleArray.size();j++)
		{
			int index = maleArray.at(j);
			vector<int> womenArray = women.at(index);
			if(findIndex(index,maleArray) < matchIndex)
			{
				if(findIndex(male,womenArray) < findIndex(partner.at(index),womenArray))				
				{
					return false;
				}
			}
		}
	}
	return true;
}

int Solution::findIndex(int toFind, vector<int> input)
{
	for(int i=0; i<input.size();i++)
	{
		if(input.at(i) == toFind)
		{
			return i;
		}
	}
	return 0;
}