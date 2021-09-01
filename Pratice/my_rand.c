#include "Yap/YapInterface.h"   // header file for the Yap interface to C
#include <stdlib.h>

int c_my_random(void) 
{
YAP_Term number = YAP_MkIntTerm(rand());
return(YAP_Unify(YAP_ARG1,number));
}
void init_predicates() 
{
YAP_UserCPredicate("my_random",c_my_random,1);
}
