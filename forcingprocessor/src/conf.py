{
    "forcing"  : {
        "forcing_type" : "operational_archive",
        "start_date"   : "202310030000",
        "end_date"     : "202310030000",
        "nwm_file"     : "",
        "runinput"     : 1,
        "varinput"     : 5,
        "geoinput"     : 1,
        "meminput"     : 0,
        "urlbaseinput" : 7,
        "fcst_cycle"   : [0],
        "lead_time"    : [1, 2, 3, 4, 5, 6],
        "weight_file"  : "01_weights.json"

    },

    "storage":{
        "storage_type"       : "S3",
        "output_bucket"      : "ngenforcingdev",
        "output_bucket_path" : "AWI_18hr",
        "cache_bucket"       : "ngenresourcesdev",
        "cache_bucket_path"  : "",
        "output_file_type"   : "csv"
    },    

    "run" : {
        "verbose"       : true,
        "check_files"   : true,
        "collect_stats" : true,
        "secret_name"   : "jlaser_creds",
        "region_name"   : "us-west-2",
        "proc_threads"  : 54,
        "write_threads" : 96,
        "nfile_chunk"   : 720
    }
}

