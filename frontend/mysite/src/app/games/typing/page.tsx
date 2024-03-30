'use client';

// import { useEffect } from "react";
import { useSearchParams, useRouter } from "next/navigation";

export default function Typing() {
  const searchParams = useSearchParams();
  const myParam = searchParams.get("charlength") as string;
  const router = useRouter();
  // useEffect(() => {
    const validParams = ['25', '50', '100', '200'];
    if(!myParam) {
      router.push('/games/?error=noparam');
    } else if(!validParams.includes(myParam)) {
      router.push('/games/?error=invalidparam')
    }
  // }, [myParam, router])
  return (
    <>
      <h1>This will contain the canvas for typing game.</h1>
      { myParam && <p>The number of characters is {myParam}.</p>}
    </>
  );
};