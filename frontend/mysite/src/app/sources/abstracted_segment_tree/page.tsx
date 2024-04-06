import Head from "next/head"
import Script from "next/script"

export default function Abstracted_segment_tree() {
  return (
    <>
      <Script src="https://cdn.jsdelivr.net/gh/google/code-prettify@master/loader/run_prettify.js"></Script>
      <h1>抽象化セグメントツリー</h1>
      <p>テンプレートを用いて抽象化したセグメントツリー。内部構造を書き換える手間を減らせる。</p>
      <code>
        <pre className="prettyprint lang-cpp">
          {`
            template<typename T>
            class SegmentTree{
              using F = function<T(T, T)>;
              public:
              void construct(F f, T initial_value, int number_of_datum){
                n = 1;
                identity_element = initial_value;
                while(n < number_of_datum) n *= 2;
                dat.assign(2 * n - 1, identity_element);
                func = f;
              }
              void point_update(int index, T value){
                index += n - 1;
                dat[index] = value;
                while(index > 0){
                  index = (index - 1) / 2;
                  dat[index] = func(dat[2 * index + 1], dat[2 * index + 2]);
                }
              }
              T range_query(int s, int t){
                return inner_range_query(s, t + 1, 0, 0, n);
              }
              T point_get_value(int index){
                return dat[index + n - 1];
              }
              private:
              int n;
              F func;
              T identity_element;
              vector<T> dat;
              T inner_range_query(int a, int b, int k, int l, int r){
                if(r <= a || b <= l) return identity_element;
                if(a <= l && r <= b) return dat[k];
                T vl = inner_range_query(a, b, 2 * k + 1, l, (l + r) / 2);
                T vr = inner_range_query(a, b, 2 * k + 2, (l + r) / 2, r);
                return func(vl, vr);
              }
            };
          `}
        </pre>
      </code>
    </>
  )
}