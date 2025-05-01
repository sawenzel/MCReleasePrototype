#JDL_PACKAGE=O2sim::v20250430-1
#JDL_OUTPUT=*@disk=1

host=`hostname -a`
echo "Hello world from ${host}"
if (( RANDOM % 2 == 0 )); then
  echo "Exiting with status 1"
  exit 1
fi
exit 0
