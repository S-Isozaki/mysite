'use client';

import Link from "next/link"
import { useSearchParams, useRouter } from "next/navigation"

export default function Games() {
  const searchParams = useSearchParams();
  const error = searchParams.get("error");
  let errorMsg = '';
  if(error == 'noparam') {
    errorMsg = 'no parameter is set';
  } else if(error == 'invalidparam') {
    errorMsg = 'invalid parameter is set'
  }
  return (
    <>
      <Link href={'/games/typing'}>typing game</Link>
      { errorMsg && <p>Error: { errorMsg }</p>}
    </>
  )
}