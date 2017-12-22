#include <atlbase.h>
#include <atlapp.h>
#include <atluser.h>
#include <iostream>

int main(int argc, char **argv)
{
  auto cursor = WTL::AtlLoadSysCursor(IDC_ARROW);
  std::cout << "IDC_ARROW cursor handle " << cursor << std::endl;

  return 0;
}
