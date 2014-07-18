select SUM(Acount*Bcount) as value from (
	select A.docid Adocid, B.docid Bdocid, A.term Aterm, B.term Bterm, A.count Acount, B.count Bcount
	from frequency A, frequency B
	where A.term = B.term -- Join column to column because it's transposed
		--and a.docid < B.docid -- Optimization for simetrical matrix
		and a.docid = '10080_txt_crude' and B.docid = '17035_txt_earn'
	--group by Adocid, Bterm;
) x
